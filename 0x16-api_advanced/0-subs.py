#!/usr/bin/python3
"""
returns the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Nate request"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        elif response.status_code == 404:
            return 0
        else:
            return 0
    
    except requests.RequestException:
        return 0

