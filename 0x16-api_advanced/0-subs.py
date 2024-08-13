#!/usr/bin/python3
"""
Returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ Function that GETS subscriber count """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Nate request"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    results = res.json().get("data")
    return results.get("subscribers")

