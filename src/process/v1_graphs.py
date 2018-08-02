from src.model.dao import *

import matplotlib.pyplot as py
import numpy

def most_common_words_by_subreddit(subreddit):
    word_count = {}
    comments = get_comment_by_subreddit(subreddit)
    for comment in comments:
        words = comment.text.split()
        for word in words:
            if(word not in word_count):
                word_count[word] = 1
            else:
                word_count[word] += 1

    sorted_word_count = list(reversed(sorted(word_count.items(),key=lambda k_v: k_v[1])))

    x_axis = map(lambda k_v : k_v[0],sorted_word_count)
    y_axis = map(lambda k_v : k_v[1],sorted_word_count)

    y_pos = numpy.arange(len(x_axis))

    py.bar(y_pos, y_axis, align="center")

    py.ylabel("occurrences")
    py.xlabel("words")
    py.title("most common words for /r/" + subreddit)
    py.xticks(y_pos, x_axis)
    py.gcf().set_size_inches(30, 30)
    py.savefig("./graph")
