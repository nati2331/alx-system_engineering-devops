#!/usr/bin/python3
"""prints titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """
        prints titles of the first 10 hot posts
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
