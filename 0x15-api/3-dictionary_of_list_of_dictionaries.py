#!/usr/bin/python3
"""
A Python script that uses a REST API, for a
given employee ID to return information about
his/her TODO list progress.
"""


if __name__ == "__main__":
    import json
    import requests

    usersUrl = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(usersUrl)
    users = response.json()

    myJSONdict = {}
    for user in users:
        userId = user.get('id')
        username = user.get('username')
        userUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                userId)
        userTodoUrl = str(userUrl + "/todos")
        userTodoDetails = requests.get(userTodoUrl)
        userTodoDetailsJSON = userTodoDetails.json()
        myJSONdict[userId] = []
        for task in userTodoDetailsJSON:
            myJSONdict[userId].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
                })
    with open('todo_all_employees.json', 'w') as myJSONFile:
        json.dump(myJSONdict, myJSONFile)
