#!/usr/bin/python3


import requests


def number_of_subscribers(subreddit):
    """returns no. of subs for a given subreddit"""
    api_url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "Windows/11"}
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    response_json = response.json()
    if response.status_code != 200:
        return (0)
    if 'data' in response_json:
        return (response_json.get('data').get('subscribers'))
