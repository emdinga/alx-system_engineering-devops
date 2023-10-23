#!/usr/bin/python3
""" to do list """

import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee data
    response_employee = requests.get(employee_url)
    if response_employee.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    employee_data = response_employee.json()
    employee_name = employee_data["name"]

    # Fetch TODO list for the employee
    response_todos = requests.get(todos_url)
    if response_todos.status_code != 200:
        print(f"Error: Unable to fetch TODO list for employee {employee_name}.")
        return

    todos_data = response_todos.json()

    # Calculate TODO progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task["completed"])

    # Display progress information
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

    # Display completed task titles
    for task in todos_data:
        if task["completed"]:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)

