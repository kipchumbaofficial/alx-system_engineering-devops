#!/usr/bin/python3
'''Fetches the hot subreddits
in a subreddit
'''
import requests
import sys


def top_ten(subreddit):
    '''Returns top ten hot posts'''

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; '
    user += 'rv:114.0) Gecko/20100101 Firefox/114.0'
    headers = {
            'User-Agent': user
            }
    parameters= {'limit': 10}
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=parameters)

    if response.status_code == 200:
        retval = response.json().get('data').get('children')
        for posts in retval:
            print(posts.get('data').get('title'))
    else:
        print(None)
