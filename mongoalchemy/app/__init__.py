from flask import Flask
from flask_mongoalchemy import MongoAlchemy
import os, sys, inspect
from passlib.hash import des_crypt as pwd_context
from passlib.apps import custom_app_context as pwd_admin
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['DEBUG'] = True
app.config['MONGOALCHEMY_DATABASE'] = 'testMongo'

db = MongoAlchemy(app)

import models

from app.mod_test.controllers import mod_test as test
app.register_blueprint(test)
