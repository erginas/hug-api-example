import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from models import Author,Book,Base
from schemas import AuthorSchema,BookSchema
import json
import hug
engine = sa.create_engine('sqlite:///:db.db:')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session= DBSession()



@hug.get()
def getbooks():
    books = session.query(Book).all()
    bookschema = BookSchema(many=True)
    return json.dumps(bookschema.dump(books).data)
