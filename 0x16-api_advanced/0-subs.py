#!/usr/bin/python3
'''Fetches the number of subscribers
in a subreddit
'''
import requests


def number_of_subscribers(subreddit):
    '''Returns the number of subscribers
    or 0 if the subreddit is invalid'''

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; '
    user += 'rv:114.0) Gecko/20100101 Firefox/114.0'
    headers = {
            'User-Agent': user
            }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        retval = response.json()
        return retval['data']['subscribers']
    else:
        return 0
