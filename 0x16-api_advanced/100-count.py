#!/bin/usr/python3
""" fetch hot articles"""

import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively fetch hot articles from a subreddit

    :param subreddit: The name of the subreddit to query.
    :param word_list: List of keywords
    """
    if word_counts is None:
        word_counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            words = title.lower().replace('.', ' ').replace('!', ' ').replace('_', ' ').split()
            
            for word in word_list:
                if word.lower() in words:
                    word_counts[word] += words.count(word.lower())

        after = data['data']['after']

        if after is not None:
            return count_words(subreddit, word_list, after, word_counts)
        else:
            for word, count in sorted(word_counts.items(), key=lambda item: (-item[1], item[0])):
                print(f"{word}: {count}")
