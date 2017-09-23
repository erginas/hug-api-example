import hug
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationships
from sqlalchemy import create_engine

Base = declarative_base()


class Members(Base):
    __tablename__ = 'members'
    id = Column(Integer,primary_key=True)
    member_name = Column(String(25), nullable=False)
    member_email = Column(String(35),nullable=False)
    member_password = Column(String(500))
    def __json__(self):
        return ['member_name','member_email','member_password']

class Articles(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    article_name = Column(String(100), nullable=False)
    article_content = Column(String(0))
    article_img = Column(String(0))
    author = relationships
    def __json__(self):
        return ['article_name','article_content','article_img','author']

engine = create_engine('sqlite:///example.db')

Base.metadata.create_all(engine)