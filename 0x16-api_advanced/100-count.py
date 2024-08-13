#!/usr/bin/python3
"""
counts the occurrences of specific words.
"""

import requests
import sys

def count_words(subreddit, word_list):
    """
    Counts the occurrences of each word in word_list from the titles of the
    first 100 hot posts for a given subreddit.
    """
    after = None
    word_list = [word.lower() for word in word_list]
    word_count = {word: 0 for word in word_list}
    
    headers = {'User-Agent': 'Nate request'}
    base_url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)

    while True:
        url = base_url
        if after:
            url += "&after={}".format(after)
        
        try:
            response = requests.get(url, headers=headers, allow_redirects=False)
            
            if response.status_code != 200:
                print("None")
                return
            
            data = response.json()
            if 'data' not in data or 'children' not in data['data']:
                print("None")
                return
            
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    word_count[word] += title.split().count(word)
            
            after = data['data'].get('after')
            if not after:
                break
        
        except requests.RequestException:
            print("None")
            return
    
    for word in word_list:
        print("{}: {}".format(word, word_count[word]))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 100-main.py <subreddit> <word1> <word2> ...")
    else:
        subreddit = sys.argv[1]
        words = sys.argv[2:]
        count_words(subreddit, words)

