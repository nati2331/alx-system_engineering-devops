#!/usr/bin/python3
"""
API word count
"""

import re
import requests


def count_words(subreddit, word_list, after='', word_count={}):
    """
    Print the count of each keyword in descending order.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {"User-Agent": "Nate request"}

    subreddit_info = requests.get(url, headers=headers, allow_redirects=False)

    if subreddit_info.status_code == 200:
        data = subreddit_info.json().get('data', {})
        posts = data.get('children', [])
        if posts:
            for post in posts:
                title = post.get('data', {}).get('title', '').lower()
                for word in word_list:
                    word = word.lower()
                    if re.search(rf"\b{word}\b", title):
                        word_count[word] = word_count.get(word, 0) + 1

            after = data.get('after')
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    print(f"{word}: {count}")
        else:
            pass
    else:
        pass
