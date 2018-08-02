#!/usr/bin/env python


import argparse
import requests
import sys
import string

parser = argparse.ArgumentParser(prog='PROG')
subparsers = parser.add_subparsers(help='sub-command help')

mcwbs = subparsers.add_parser('mcwbs', help='Most common words by subreddit')
mcwbs.add_argument('-s','--subreddit')

def most_common_words_by_subreddit(subreddit):
    message = requests.get("http://localhost:5000/most-common-words-by-subreddit/" + subreddit)


if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])
    if(sys.argv[1] == "mcwbs"):
        most_common_words_by_subreddit(args.subreddit)

