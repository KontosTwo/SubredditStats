import praw

reddit = praw.Reddit(client_id="pq6yMqlqnqgVxg",
                     client_secret="wnW1EokkShH7wYdQXs52ofxNyfs",
                     username="SStats",
                     password="000000",
                     user_agent="Kiki"
                     )


def get_reddit():
    return reddit