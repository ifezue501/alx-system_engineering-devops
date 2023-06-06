#!/usr/bin/python3

"""
Recursive function to query the Reddit API, parse the titles of hot articles,
and print a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries the Reddit API, parses the titles of hot articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): List of keywords to count.
        after (str): The "after" parameter value for pagination (default: None).
        counts (dict): Dictionary to store the count for each keyword (default: None).

    Returns:
        None
    """

    if counts is None:
        counts = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                count = title.count(word.lower())
                if word.lower() not in counts:
                    counts[word.lower()] = count
                else:
                    counts[word.lower()] += count

        after = data["data"]["after"]
        if after is not None:
            count_words(subreddit, word_list, after, counts)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
