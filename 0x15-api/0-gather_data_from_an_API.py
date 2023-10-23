#!/usr/bin/python3
"""
Retrieve employees list 
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays employee's TODO list progress.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None
    """
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{main_url}/todos?userId={employee_id}"
    name_url = f"{main_url}/users/{employee_id}"
    
    todo_result = requests.get(todo_url).json()
    name_result = requests.get(name_url).json()

    todo_num = len(todo_result)
    todo_complete = sum(1 for todo in todo_result if todo["completed"])
    name = name_result["name"]

    print(f"Employee {name} is done with tasks({todo_complete}/{todo_num}):")
    
    for todo in todo_result:
        if todo["completed"]:
            print(f"\t {todo['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

