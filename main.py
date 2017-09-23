import hug
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from dbcreate import Articles, Members, Base

engine =  create_engine('sqlite:///example.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()


def to_json(self, rel=None):
    def extended_encoder(x):
        if isinstance(x, datetime):
            return x.isoformat()
        if isinstance(x, UUID):
            return str(x)

    if rel is None:
        rel = self.RELATIONSHIPS_TO_DICT
    return json.dumps(self.to_dict(rel), default=extended_encoder)
@hug.get()
def articles(id= hug.types.number):
    allarticles = session.query(Articles).all()
    allarticles = to_json(allarticles)
    return allarticles
