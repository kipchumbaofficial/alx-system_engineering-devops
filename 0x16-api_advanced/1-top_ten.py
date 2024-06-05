#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""


from requests import get


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the
    4 titles of the first 10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    limit = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # , allow_redirects=False)
    response = get(url, headers=headers, params=limit)
    results = response.json()

    try:
        topTen = results.get('data').get('children')
        for post in topTen:
            print(post.get('data').get('title'))
    except Exception:
        print("None")
