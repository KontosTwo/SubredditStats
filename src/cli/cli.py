#!/usr/bin/env python


import click
import requests

def main():
    pass

@click.command()
@click.option('--subreddit', prompt="Subreddit")
def most_common_words_by_subreddit(subreddit):
    message = requests.get("http://localhost:5000/most-common-words-by-subreddit/" + subreddit)
    print(message.content)

if __name__ == "__main__":
    most_common_words_by_subreddit()