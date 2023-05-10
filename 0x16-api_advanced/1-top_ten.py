#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """return as menstioned"""
    api_url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
    headers = {'User-Agent': 'Windows/11'}
    params = {'limit': 10}
    response = requests.get(
            api_url, allow_redirects=False, headers=headers, params=params)
    # print(response)
    if response.status_code != 200:
        return (0)
    response = response.json()

    if 'data' in response:
        for titles in response.get('data').get('children'):
            print(titles.get('data').get('title'))
    else:
        return (0)
