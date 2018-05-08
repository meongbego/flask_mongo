from flask import Blueprint, request, g, session, redirect, url_for,abort, render_template
from flask import jsonify
from app import db, auth
from app.paginate import Paginate
from app.models import *
import json
import re


mod_test = Blueprint('test', __name__, url_prefix='/test', template_folder='./templates')

@mod_test.route('/new_user', methods = ['POST'])
def new_user():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    user = User(email=email,first_name=first_name,last_name=last_name)
    user.save()
    return 'saved :)'
