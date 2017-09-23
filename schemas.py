from marshmallow_sqlalchemy import ModelSchema
from models import Author,Book




class BookSchema(ModelSchema):

    class Meta:
        model = Book


class AuthorSchema(ModelSchema):
    class Meta:
        model = Author

