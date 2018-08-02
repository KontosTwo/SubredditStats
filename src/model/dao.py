from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.model.model import CommentRef, Base, Comment, engine

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
Session.bind = engine

def store_commentref(commentref: CommentRef):
    session = Session()
    try:
        session.add(commentref)

        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def stream_commentref():
    session = Session()
    query = session.query(CommentRef)
    return query_stream(query)

def store_comment(comment: Comment):
    session = Session()
    try:
        session.add(comment)

        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def get_comment_by_subreddit(subreddit):
    session = Session()
    query = session.query(Comment).filter(Comment.subreddit == subreddit)


    session.close()
    return query.all()

def query_stream(q):
    offset = 0
    while True:
        r = False
        for elem in q.limit(100).offset(offset):
            r = True
            yield elem
        offset += 100
        if not r:
            break