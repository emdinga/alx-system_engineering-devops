#!/usr/bin/python3
"""Returns to-do list"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    
    total_tasks = len(todos)
    completed_tasks = len(completed)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), completed_tasks, total_tasks))

    for c in completed:
        print("\t{}".format(c))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)

