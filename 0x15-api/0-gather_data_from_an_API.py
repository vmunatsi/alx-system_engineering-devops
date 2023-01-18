#!/usr/bin/python3
""" Module 0 """
from requests import get
import sys


if __name__ == "__main__":
    data = get('https://jsonplaceholder.typicode.com/users/{}'
               .format(sys.argv[1])).json()
    request = get('https://jsonplaceholder.typicode.com/todos/?userId={}'
                  .format(sys.argv[1]))
    all_tasks = request.json()
    completed = [task for task in all_tasks if task.get('completed')]
    print("Employee {} is done with tasks({}/{}):"
          .format(data.get('name'), len(completed), len(all_tasks)))
    for task in completed:
        print("\t{}".format(task.get('title')))
