from datetime import datetime
from app import db
from flask_mongoalchemy import BaseQuery
import re

class Author(db.Document):
    name = db.StringField()

    @property
    def serialize(self):
        return {
            'name': self.name
        }
    def __repr__(self):
        return "<Author(name='%s')>" % self.name

class Label(db.Document):
    label = db.StringField()

    @property
    def serialize(self):
        return {
            'label': self.label
        }

    def __repr__(self):
        return "<Label(name='%s')>" % self.label

class Book(db.Document):
    title = db.StringField()
    year = db.StringField()
    label = db.ListField(db.DocumentField(Label))
    author = db.ListField(db.DocumentField(Author))
