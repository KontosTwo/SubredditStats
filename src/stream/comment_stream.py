from src.stream.reddit import get_reddit
from src.model.model import CommentRef
import threading

from src.model.dao import store_commentref
reddit = get_reddit();
subreddit = reddit.subreddit("all")

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
            comment = next(self.stream)
            self.__store_comment_ref(comment)

    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()  # unblock self if waiting

    def pause(self):
        with self.state:
            self.paused = True  # make self block and wait

    def __store_comment_ref(self,comment):
        comment_ref = CommentRef(
            comment_id=comment.id,
            subreddit=comment.subreddit.display_name,
            date=comment.created,
            author=comment.author.name
        )
        store_commentref(comment_ref)



concur = Concur(subreddit.stream.comments())
concur.start() # calls run() method

def start_stream():
    concur.resume()


def stop_stream():
    concur.pause()