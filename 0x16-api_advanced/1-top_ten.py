#!/usr/bin/python3
"""  function that queries the Reddit API and prints the titles of the first 10 hot posts 
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if posts:
            print(f"Top 10 hot posts in r/{subreddit}:\n")
            for post in posts:
                title = post['data']['title']
                print(f"- {title}")
        else:
            print(f"No hot posts found in r/{subreddit}.")
    else:
        print("Invalid subreddit or not found.")
