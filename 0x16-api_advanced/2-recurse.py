#!/usr/bin/python3
"""recursive function that returns a list containing the titles """

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles"""
    url = "https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Nate request"}

    subreddit_info = requests.get(url, headers=headers, allow_redirects=False)

    if subreddit_info.status_code == 200:
        data = subreddit_info.json().get('data', {})
        posts = data.get('children', [])
        if posts:
            for post in posts:
                hot_list.append(post.get('data', {}).get('title'))

            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None
    else:
        return None
