import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from models import Author,Book,Base
from schemas import AuthorSchema,BookSchema
import json
import hug
from falcon import *
engine = sa.create_engine('sqlite:///:db.db:')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session= DBSession()



@hug.get('/books')
def getbooks():
    books = session.query(Book).all()
    bookschema = BookSchema(many=True)
    return json.dumps(bookschema.dump(books).data)


@hug.post('/books')
def addbooks(body):
    id = body['author_id']
    bookname = body['bookname']
    try:
        author = session.query(Author).filter_by(id=id).first()

        book = Book(name=bookname,author_id=author_id,author=author.name)
        return HTTP_202
    except TypeError:
        return HTTP_404
@hug.post('/authors')
def addauthors(body):
    session.rollback()
    author_name = body['author_name']
    author = Author(name=author_name)
    session.add(author)
    session.commit()
    return HTTP_202