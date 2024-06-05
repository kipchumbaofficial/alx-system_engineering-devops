#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given
subreddit
"""


from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    response = get(url, headers=headers)

    if response.status_code == 200:
        results = response.json()
        for children in results.get('data').get('children'):
            hot_list.append(children.get("data").get("title"))

        after = results.get('data').get('after')

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
