#!/usr/bin/python3
'''Fetches the number of subscribers
in a subreddit
'''

from requests import get


def number_of_subscribers(subreddit):
    """"Returns:
        The number of subscribers, or 0 if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=headers, allow_redirects=False)
    results = response.json()

    try:
        return results.get('data').get('subscribers')
    except Exception:
        return 0
