#!/usr/bin/python3
'''Gather data from an API
'''


if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    url = 'https://jsonplaceholder.typicode.com/users/'

    todos = requests.get(f'{url}{argv[1]}/todos')
    user = requests.get(f'{url}{argv[1]}')

    tasks = todos.json()
    info = user.json()

    csv_file = f'{argv[1]}.csv'

    with open(csv_file, mode='w', newline='') as file_csv:
        writer = csv.writer(file_csv, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([task.get("userId"), info.get("name"),
                            task.get("completed"), task.get("title")])
