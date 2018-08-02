from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CommentRef(Base):
    __tablename__ = 'commentref'


    comment_id = Column(String(250), primary_key=True)
    subreddit = Column(String(250))
    date = Column(Integer)
    author = Column(String(250))

class Comment(Base):
    __tablename__ = 'comment'

    comment_id = Column(String(250), primary_key=True)
    subreddit = Column(String(250))
    date = Column(Integer)
    author = Column(String(250 ))
    edited = Column(Boolean)
    gilded = Column(Boolean)
    text = Column(String(10000))
    controversiality = Column(Boolean)
    upvotes = Column(Integer)


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

