#!/usr/bin/python3
'''Gather data from an API
'''


if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    url = 'https://jsonplaceholder.typicode.com/users/'

    user = requests.get(f'{url}{argv[1]}')
    todos = requests.get(f'{url}{argv[1]}/todos')

    info = user.json()
    tasks = todos.json()

    task_format = [{"task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": info.get('name')}
                   for task in tasks]
    retval = {}
    retval[argv[1]] = task_format
    with open(f'{argv[1]}.json', 'w') as jsonfile:
        json.dump(retval, jsonfile)
