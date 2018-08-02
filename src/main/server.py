from flask import Flask,request
from src.process.v1_graphs import *

app = Flask(__name__)

@app.route('/most-common-words-by-subreddit')
def index():
    most_common_words_by_subreddit(request.args["subreddit"])

if __name__ == '__main__':
    app.run(debug=True)