from flask import Flask,request
from src.process import v1_graphs
from src.stream.comment_stream import *

app = Flask(__name__)

@app.route('/start-stream')
def start_stream():
    start_stream()

@app.route('/stop-stream')
def stop_stream():
    stop_stream()

@app.route('/start-update')
def start_update():
    start_update()

@app.route('/stop-update')
def stop_update():
    stop_update()

@app.route('/most-common-words-by-subreddit/<subreddit>')
def most_common_words_by_subreddit(subreddit):
    v1_graphs.most_common_words_by_subreddit(subreddit)
    return 'Success'

if __name__ == '__main__':
    app.run(debug=True)