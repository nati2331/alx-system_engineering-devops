#!/usr/bin/python3
"""
Prints titles of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'user-agent': 'Nate request'}
    req = requests.get(url, headers=headers)
    if (req.status_code == 404):
        print("None")
    elif 'data' not in req.json():
        print("None")
    else:
        req = req.json()
        for post in req['data']['children']:
            print(post['data']['title'])
