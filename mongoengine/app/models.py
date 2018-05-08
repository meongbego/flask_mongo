from datetime import datetime
from app import db
import re

class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)

class Content(db.EmbeddedDocument):
    text = db.StringField()
    lang = db.StringField(max_length=3)

class Post(db.Document):
    title = db.StringField(max_length=120, required=True)
    author = db.ReferenceField(User)
    tags = db.ListField(db.StringField(max_length=30))
    content = db.EmbeddedDocumentField(Content)
