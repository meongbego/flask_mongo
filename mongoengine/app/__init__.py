from flask import Flask
import os, sys, inspect
from passlib.hash import des_crypt as pwd_context
from passlib.apps import custom_app_context as pwd_admin
from flask_httpauth import HTTPBasicAuth

from flask_mongoengine import MongoEngine


app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['MONGODB_DB'] = 'testMongoEngine'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017
# app.config['MONGODB_USERNAME'] = ''
# app.config['MONGODB_PASSWORD'] = ''
app.config['DEBUG'] = True

db = MongoEngine(app)

import models

from app.mod_test.controllers import mod_test as test
app.register_blueprint(test)
