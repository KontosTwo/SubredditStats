from src.model.dao import *

import matplotlib.pyplot as py
import numpy
import json
import re

def most_common_words_by_subreddit(subreddit):
    word_count = {}
    comments = None
    if (subreddit == "all"):
        comments = get_all_comments()
    else:
        comments = get_comment_by_subreddit(subreddit)
    for comment in comments:
        words = comment.text.lower().split()
        for word in words:
            if word in functional_words:
                continue
            if(word not in word_count):
                word_count[word] = 1
            else:
                word_count[word] += 1

    sorted_word_count = list(reversed(sorted(word_count.items(),key=lambda k_v: k_v[1])))

    x_axis = [i[0] for i in sorted_word_count]
    y_axis = [i[1] for i in sorted_word_count]

    y_pos = numpy.arange(len(x_axis))

    py.bar(y_pos, y_axis, align="center")
    py.xticks(rotation=90)
    py.ylabel("occurrences")
    py.xlabel("words")
    py.title("most common words for /r/" + subreddit)
    py.xticks(y_pos, x_axis)
    py.gcf().set_size_inches(60, 30)
    py.savefig("./graph")
    py.close()


def word_appearance_to_upvotes(subreddit):
    comments = None
    if(subreddit == "all"):
        comments = get_all_comments()
    else:
        comments = get_comment_by_subreddit(subreddit)

    word_upvotes = {}
    for comment in comments:
        words = comment.text.lower().split()


        for word in words:
            if word in functional_words:
                continue
            if (word not in word_upvotes):
                word_upvotes[word] = comment.upvotes
            else:
                word_upvotes[word] += comment.upvotes

    sorted_word_upvotes = list(reversed(sorted(word_upvotes.items(),key=lambda k_v: k_v[1])))
    trimmed = sorted_word_upvotes[:50]

    x_axis = [i[0] for i in trimmed]
    y_axis = [i[1] for i in trimmed]

    y_pos = numpy.arange(len(x_axis))

    py.bar(y_pos, y_axis, align="center")
    py.xticks(rotation=90)
    py.ylabel("total upvotes")
    py.xlabel("word")
    py.title("most upvoted words in /r/" + subreddit)
    py.xticks(y_pos, x_axis)
    py.gcf().set_size_inches(60, 30)
    py.savefig("./graph")
    py.close()

def word_controversiality(subreddit):
    comments = None
    if (subreddit == "all"):
        comments = get_all_comments()
    else:
        comments = get_comment_by_subreddit(subreddit)

    word_controversiality = {}
    for comment in comments:
        words = comment.text.lower().split()
        for word in words:
            if word in functional_words:
                continue
            if (word not in word_controversiality):
                word_controversiality[word] = 1 if comment.controversiality else 0
            else:
                word_controversiality[word] += 1 if comment.controversiality else 0

    sorted_word_controversiality = list(reversed(sorted(word_controversiality.items(), key=lambda k_v: k_v[1])))
    trimmed = sorted_word_controversiality[:50]

    x_axis = [i[0] for i in trimmed]
    y_axis = [i[1] for i in trimmed]

    y_pos = numpy.arange(len(x_axis))

    py.bar(y_pos, y_axis, align="center")
    py.xticks(rotation=90)
    py.ylabel("total upvotes")
    py.xlabel("word")
    py.title("most upvoted words in /r/" + subreddit)
    py.xticks(y_pos, x_axis)
    py.gcf().set_size_inches(60, 30)
    py.savefig("./graph")
    py.close()



functional_words = {
'*',
'a' ,
'about' ,
'above' ,
'across' ,
'after' ,
'afterwards' ,
'again' ,
'against' ,
'all' ,
'almost' ,
'alone' ,
'along' ,
'already' ,
'also' ,
'although' ,
'always' ,
'am' ,
'among' ,
'amongst' ,
'amoungst' ,
'an' ,
'and' ,
'another' ,
'any' ,
'anyhow' ,
'anyone' ,
'anything' ,
'anyway' ,
'anywhere' ,
'are' ,
'around' ,
'as' ,
'at' ,
'be' ,
'became' ,
'because' ,
'been' ,
'before' ,
'beforehand' ,
'behind' ,
'being' ,
'below' ,
'beside' ,
'besides' ,
'between' ,
'beyond' ,
'both' ,
'but' ,
'by' ,
'can' ,
'cannot' ,
'could' ,
'dare' ,
'despite' ,
'did' ,
'do' ,
'does' ,
'done' ,
'down' ,
'during' ,
'each' ,
'eg' ,
'either' ,
'else' ,
'elsewhere' ,
'enough' ,
'etc' ,
'even' ,
'ever' ,
'every' ,
'everyone' ,
'everything' ,
'everywhere' ,
'except' ,
'few' ,
'first' ,
'for' ,
'former' ,
'formerly' ,
'from' ,
'further' ,
'furthermore' ,
'had' ,
'has' ,
'have' ,
'he' ,
'hence' ,
'her' ,
'here' ,
'hereabouts' ,
'hereafter' ,
'hereby' ,
'herein' ,
'hereinafter' ,
'heretofore' ,
'hereunder' ,
'hereupon' ,
'herewith' ,
'hers' ,
'herself' ,
'him' ,
'himself' ,
'his' ,
'how' ,
'however' ,
'i' ,
'ie' ,
'if' ,
'in' ,
'indeed' ,
'inside' ,
'instead' ,
'into' ,
'is' ,
'it' ,
'it\'s' ,
'itself' ,
'last' ,
'latter' ,
'latterly' ,
'least' ,
'less' ,
'lot' ,
'lot\'s' ,
'many' ,
'may' ,
'me' ,
'meanwhile' ,
'might' ,
'mine' ,
'more' ,
'moreover' ,
'most' ,
'mostly' ,
'much' ,
'must' ,
'my' ,
'myself' ,
'namely' ,
'near' ,
'need' ,
'neither' ,
'never' ,
'nevertheless' ,
'next' ,
'no' ,
'nobody' ,
'none' ,
'noone' ,
'nor' ,
'not' ,
'nothing' ,
'now' ,
'nowhere' ,
'of' ,
'off' ,
'often' ,
'oftentime' ,
'on' ,
'one' ,
'only' ,
'onto' ,
'or' ,
'other' ,
'others' ,
'otherwise' ,
'ought' ,
'our' ,
'ours' ,
'ourselves' ,
'out' ,
'outside' ,
'over' ,
'per' ,
'perhaps' ,
'rather' ,
're' ,
'same' ,
'second' ,
'several' ,
'shall' ,
'she' ,
'should' ,
'since' ,
'so' ,
'some' ,
'somehow' ,
'someone' ,
'something' ,
'sometime' ,
'sometimes' ,
'somewhat' ,
'somewhere' ,
'still' ,
'such' ,
'than' ,
'that' ,
'the' ,
'their' ,
'theirs' ,
'them' ,
'themselves' ,
'then' ,
'thence' ,
'there' ,
'thereabouts' ,
'thereafter' ,
'thereby' ,
'therefore' ,
'therein' ,
'thereof' ,
'thereon' ,
'thereupon' ,
'these' ,
'they' ,
'third' ,
'this' ,
'those' ,
'though' ,
'through' ,
'throughout' ,
'thru' ,
'thus' ,
'to' ,
'together' ,
'too' ,
'top' ,
'toward' ,
'towards' ,
'under' ,
'until' ,
'up' ,
'upon' ,
'us' ,
'used' ,
'very' ,
'via' ,
'was' ,
'we' ,
'well' ,
'were' ,
'what' ,
'whatever' ,
'when' ,
'whence' ,
'whenever' ,
'where' ,
'whereafter' ,
'whereas' ,
'whereby' ,
'wherein' ,
'whereupon' ,
'wherever' ,
'whether' ,
'which' ,
'while' ,
'whither' ,
'who' ,
'whoever' ,
'whole' ,
'whom' ,
'whose' ,
'why' ,
'whyever' ,
'will' ,
'with' ,
'within' ,
'without' ,
'would' ,
'yes' ,
'yet' ,
'you' ,
'your' ,
'yours' ,
'yourself' ,
'yourselves' ,
}