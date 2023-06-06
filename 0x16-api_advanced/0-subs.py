#!/usr/bin/python3


import requests


def number_of_subscribers(subreddit):
    """returns no. of subs for a given subreddit"""
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Windows/11"}
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return (0)
    return (response.json().get('data').get('subscribers'))
