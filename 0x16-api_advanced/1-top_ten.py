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
    headers = {'User-Agent': 'Nate request'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check for HTTP status codes
        if response.status_code == 404:
            print("None")
            return
        
        # Ensure the response content is not empty
        if not response.text:
            print("None")
            return
        
        # Attempt to parse JSON
        try:
            data = response.json()
        except ValueError:
            print("None")
            return
        
        # Check if 'data' and 'children' keys exist
        if 'data' not in data or 'children' not in data['data']:
            print("None")
            return
        
        # Print the titles of the first 10 hot posts
        for post in data['data']['children']:
            print(post['data']['title'])
    
    except requests.RequestException as e:
        # Handle any other exceptions
        print("None")
        return

