#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    try:
        headers = {'User-Agent':
                   'Python:SubredditHotPosts:v1.2.3'}
        url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        [print(c['data']['title']) for c in
         response.json()['data']['children']]
    except Exception:
        print(None)
