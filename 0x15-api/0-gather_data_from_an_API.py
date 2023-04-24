#!/usr/bin/python3
"""
gathering info given employee ID
"""


import requests
import sys

if __name__ == "__main__":
    """
    do the following
    """
    api_url_user = "https://jsonplaceholder.typicode.com/users"
    api_url_todo = "https://jsonplaceholder.typicode.com/todos"
    param_todo = {'userId': sys.argv[1]}

    response_user = requests.get(
            api_url_user + '/{}'.format(sys.argv[1])).json()
    response_todo = requests.get(api_url_todo, param_todo).json()
    completed = [
            task.get('title') for task in response_todo if task.get(
                'completed') is True]

    print("Employee {} is done with tasks ({}/{})".format(
        response_user.get('name'), len(completed), len(response_todo)))
    for ttl in completed:
        print("\t {}".format(ttl))
