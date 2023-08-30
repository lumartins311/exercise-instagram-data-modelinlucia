import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



# followers_table = Table('followers', Base.metadata,
#     user_from_id =Column('follower_id', ForeignKey('users.id')),
#     user_to_id =Column('followed_id', ForeignKey('users.id'))
# )
# following_table = Table('following', Base.metadata,
#     user_from_id =Column('follower_id', ForeignKey('users.id')),
#     user_to_id =Column('followed_id', ForeignKey('users.id'))
# )
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    followers = relationship("Followers", backref="User")
    # following = relationship("User", secondary=following_table)
    
    
    

class Followers(Base):
     __tablename__ = 'followers'
     # Here we define columns for the table person
     # Notice that each column is also a normal Python instance attribute.
     id = Column(Integer, primary_key=True)
     user_from_id = Column(Integer, nullable=False, primary_key=True)
     user_to_id = Column(Integer, nullable=False, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'))
    #  relacion = relationship(Tablarelacion)



# class Tablarelacion(Base):
#     __tablename__ = 'relacion'
#     id = Column(Integer, primary_key=True)
#     user_from_id = Column(Integer, nullable=False)
#     user_to_id = Column(Integer, nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(User)
#     followers_user_to_id= Column(Integer, ForeignKey('followers.user_to_id'))
#     followers = relationship(Followers)
#     followers_user_from_id = Column(Integer, ForeignKey('followers.user_from_id'))
#     followers = relationship(Followers)

#     tags = Table('tags',
#     Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True),
#     Column('page_id', Integer, ForeignKey('page.id'), primary_key=True)
# )

# class Followers(Base):
#     id = Column(Integer, primary_key=True)
#     tags = relationship('Tag', secondary=tags, lazy='subquery',
#         backref= backref('pages', lazy=True))

# class User(Base):
#     id = Column(Integer, primary_key=True)
#     username = Column(String(250), nullable=False)
#     firstname = Column(String(250), nullable=False)
#     lastname = Column(String(250), nullable=False)
#     email = Column(String(250), nullable=False)
#     password = Column(String(250), nullable=False)


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer)
    post_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    


    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
