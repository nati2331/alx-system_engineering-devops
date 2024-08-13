#!/usr/bin/python3
" The fuction returns number of subscribers"

import requests

def number_of_subscribers(subreddit):
    """returns number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Nate request"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    results = res.json().get("data")
    return results.get("subscribers")
