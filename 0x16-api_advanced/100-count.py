#!/usr/bin/python3
""" module 100 """
import re
from requests import get


def count_words(subreddit, word_list, page=None, amount={}):
    """ top_ten - Returns the titles of the first 10 hot post
        in a subreddit.
        parameters: subreddit.
        Return: the numeber of subscribers or 0 is not a valid subreddit.
    """

    if page is None:
        request = get('https://www.reddit.com/r/{}/hot.json'
                      .format(subreddit), headers={'User-Agent': 'jdarangop'},
                      allow_redirects=False)
    else:
        request = get('https://www.reddit.com/r/{}/hot.json?after={}'
                      .format(subreddit, page),
                      headers={'User-Agent': 'jdarangop'},
                      allow_redirects=False)

    if request.status_code != 200:
        print("", end="")
    else:
        after = request.json().get('data').get('after')
        list_post = request.json().get('data').get('children')
        for i in list_post:
            title = i.get('data').get('title').lower()
            for j in word_list:
                if amount.get(j) is None:
                    amount[j] = 0
                patterns = re.findall(" {}$|^{} | {} ".format(j, j, j), title)
                if patterns != []:
                    amount[j] += len(patterns)
        if after:
            count_words(subreddit, word_list, after, amount)
        else:
            sort_alpha = sorted(amount.items(), key=lambda item: item[0])
            for key, value in sorted(sort_alpha,
                                     key=lambda item: item[1],
                                     reverse=True):
                if value != 0:
                    print("{}: {}".format(key, value))
