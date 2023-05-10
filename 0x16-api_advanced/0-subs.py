#!/usr/bin/python3
"""
return number of subs for a given subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """returns as mentioned"""
    api_url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'Windows/11'}
    response = requests.get(api_url, allow_redirects=False, headers=headers)
    # print(response)
    if response.status_code != 200:
        return (0)

    response = response.json()
    if 'data' in response:
        return (response.get('data').get('subscribers'))
    else:
        return (0)
