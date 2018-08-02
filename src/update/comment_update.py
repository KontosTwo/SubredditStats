from src.stream.reddit import get_reddit
from src.model.model import CommentRef, Comment
from src.model.dao import *
import threading


reddit = get_reddit();
subreddit = reddit.subreddit("all")




def get_comment_from_id(id):
    comment = reddit.comment(id)
    valid = comment_valid(comment)
    if(not valid):
        return
    controversiality = True if comment.controversiality == 1 else False
    gilded = True if comment.gilded == 1 else False
    edited = True if comment.edited != 0 else False
    commentObj = Comment(comment_id=comment.id,
                         upvotes=comment.ups,
                         controversiality=controversiality,
                         text=comment.body,
                         gilded=gilded,
                         author=comment.author.name,
                         subreddit=comment.subreddit.display_name,
                         date=comment.created,
                         edited=edited
                         )
    return commentObj


def comment_valid(comment):
    return (
        comment.id is not None and
        comment.ups is not None and
        comment.controversiality is not None and
        comment.body is not None and
        comment.gilded is not None and
        comment.author is not None and
        comment.author.name is not None and
        comment.subreddit is not None and
        comment.subreddit.display_name is not None and
        comment.created is not None and
        comment.edited is not None
    )



class Concur(threading.Thread):
    def __init__(self, stream):
        threading.Thread.__init__(self)
        self.iterations = 0
        self.daemon = True  # OK for main to exit even if instance is still running
        self.paused = True  # start out paused
        self.state = threading.Condition()
        self.stream = stream

    def run(self):
        while True:
            with self.state:
                if self.paused:
                    self.state.wait() # block until notified
            # do stuff
            commentref = next(self.stream)
            self.__update_commentref(commentref)

    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()  # unblock self if waiting

    def pause(self):
        with self.state:
            self.paused = True  # make self block and wait

    def __update_commentref(self,commentref):
        comment_id = commentref.comment_id
        comment = get_comment_from_id(comment_id)
        if comment is not None:
            store_comment(comment)


concur = Concur(stream_commentref())
concur.start() # calls run() method

def start_update():
    concur.resume()


def stop_update():
    concur.pause()