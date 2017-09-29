#-*- coding:utf-8 -*-
import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from models import Author,Book,Base
from schemas import AuthorSchema,BookSchema
import json
import hug
from falcon import *
engine = sa.create_engine('sqlite:///db.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session= DBSession()



@hug.get('/books')
def getbooks(response):
    books = session.query(Book).all()
    bookschema = BookSchema(many=True)
    data = bookschema.dump(books).data
    response.status = HTTP_404
    return data


@hug.post('/books')
def addbooks(body,response):
    authorid = body['author_id']
    bookname = body['bookname']
    try:
        bookname, authorid = bookname.decode(), authorid.decode()
        checkauthor = session.query(Author).filter_by(id=authorid).first()
        print(checkauthor)
        if checkauthor == None:
            response.status = HTTP_404
            return HTTP_404
        else:

            book = Book(title=bookname,author_id=authorid)
            session.add(book)
            session.commit()
            response.status = HTTP_200
            return falcon.HTTP_200
    except TypeError:
        return TypeError
@hug.post('/authors')
def addauthors(body,response):
    session.rollback()
    author_name = body['author_name']
    author = Author(name=author_name)
    session.add(author)
    session.commit()
    response.status = HTTP_202
    return falcon.HTTP_202
@hug.get('/authors')
def getauthors():
    authors = session.query(Author).all()
    authorschema = AuthorSchema(many=True)
    data = authorschema.dumps(authors).data
    return data