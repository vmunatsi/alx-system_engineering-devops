#!/usr/bin/python3
""" module 0 """
from requests import get


def number_of_subscribers(subreddit):
    """ number_of_subscribers - Returns the number of subscribers for
        a given subreddit.
        parameters: subreddit.
        Return: the numeber of subscribers or 0 is not a valid subreddit.
    """
    request = get('https://www.reddit.com/r/{}/about.json'
                  .format(subreddit), headers={'User-Agent': 'jdarangop'})

    if request.status_code != 200:
        return 0
    else:
        request_json = request.json()
        return request_json.get('data').get('subscribers')
