#!/usr/bin/python3
"""
gathering info given employee ID
"""


import csv
import requests
import sys

if __name__ == "__main__":
    """
    do the following
    """
    api_url = "https://jsonplaceholder.typicode.com/"
    # api_url_todo = "https://jsonplaceholder.typicode.com/todos"
    param_todo = {'userId': sys.argv[1]}

    user_id = sys.argv[1]
    response_user = requests.get(
            api_url + 'users/{}'.format(sys.argv[1])).json()
    username = response_user.get('username')
    response_todo = requests.get(api_url + "todos", param_todo).json()

    with open("{}.csv".format(user_id), 'w', newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, r.get("completed"), r.get(
                "title")]) for r in response_todo]
