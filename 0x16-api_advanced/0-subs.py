#!/usr/bin/python3
"""
    script that queries the Reddit API
"""


import requests


base_url = 'https://www.reddit.com/'


def number_of_subscribers(subreddit):
    """
        Function gives the number of subscribers
    """

    try:
        response = requests.get(
            url="{}/r/{}/about.json".format(base_url, subreddit),
            headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},
        )

        data = response.json()['data']

        return data['subscribers']
    except Exception:
        return False
