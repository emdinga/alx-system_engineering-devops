#!/usr/bin/python3
"""function that queries the Reddit API and returns 
    the number of subscribers """

import request


def number_of_subscribers(subreddit):
    """ 
    get the number of subscribbers for a given subreddit
    Return: number of subscribers or 0
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'Custome User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
