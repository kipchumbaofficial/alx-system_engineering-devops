#!/usr/bin/python3
'''Gather data from an API
'''


if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/users/'

    user = requests.get(f'{url}{argv[1]}')
    todos = requests.get(f'{url}{argv[1]}/todos')

    info = user.json()
    tasks = todos.json()

    total = len(tasks)
    completed = sum(1 for task in tasks if task['completed'])

    print(f"Employee {info.get('name')} is done with tasks({completed}/{total})")
    for task in tasks:
        if task['completed']:
            print(f"\t {task.get('title')}")
