#!/usr/bin/python3
""" Listing titles of first top 10 hot posts in subreddit"""


import requests


def top_ten(subreddit):
    """ listing titles"""
    api_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "windows/11"}
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    for titles in response.json().get('data').get('children'):
        print(titles.get('data').get('title'))
