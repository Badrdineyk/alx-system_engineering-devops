#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import sys


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    u_agent = (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Ubuntu Chromium/96.0.4664.110 '
        'Chrome/96.0.4664.110 Safari/537.36'
    )

    headers = {
        'User-Agent': u_agent,
        'Content-Type': 'application/x-json',
        'Accept': 'application/x-json'
    }

    url = f"https://api.reddit.com/r/{subreddit}/about.json?keyphrase=witcher"
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0

    dic = res.json()

    if 'data' not in dic:
        return 0

    if 'subscribers' not in dic.get('data'):
        return 0

    return res.json()['data']['subscribers']
