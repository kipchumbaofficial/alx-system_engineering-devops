#!/usr/bin/python3
'''Fetches the number of subscribers
in a subreddit
'''
import requests


def number_of_subscribers(subreddit):
    '''Returns the number of subscribers
    or 0 if the subreddit is invalid'''

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url)
    retval = response.json()

    if 'data' in retval and 'subscribers' in retval['data']:
        return retval['data']['subscribers']
    else:
        return 0
