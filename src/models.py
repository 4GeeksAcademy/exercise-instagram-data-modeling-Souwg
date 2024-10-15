import os
import sys
import enum
from sqlalchemy import Enum
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__= 'follower'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    User = relationship("User")

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable = False)
    firstname = Column(String(250))
    lastname =  Column(String(250))
    email = Column(String(250), unique=True, nullable=False)

class Post (Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    type = Column(Integer, ForeignKey('user.id'))
    User = relationship("User")

class Comment (Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    authord_id = Column(Integer, ForeignKey('person.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    Post = relationship("Post")
    User = relationship("User")

class MyEnum(enum.Enum):
    one = 1
    two = 2
    three = 3

class Media(Base):
    __tablename__='media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MyEnum))
    url = Column (String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    Post = relationship("Post")

    




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
