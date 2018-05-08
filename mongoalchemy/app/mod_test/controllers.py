from flask import Blueprint, request, g, session, redirect, url_for,abort, render_template
from flask import jsonify
from app import db, auth
from app.paginate import Paginate
from app.models import *
import json
import re


mod_test = Blueprint('test', __name__, url_prefix='/test', template_folder='./templates')

@mod_test.route('/new_label', methods = ['POST'])
def new_label():
    label = request.form['label']
    label = Label(label = label)
    label.save()
    return 'Saved :)'

@mod_test.route('/get_label', methods = ['GET'])
def get_label():
    label = Label.query.all()
    content = '<p>Comment:</p>'
    for i in label:
        content += '<p>%s</p>' % i
    return content

@mod_test.route('/remove_label/<id>', methods = ['GET'])
def remove_label(id):
    # label = Label.query.get_or_404(id)
    label = Label.query.filter({'label':id}).first()
    label.remove()
    # return redirect(url_for('test/get_label'))


@mod_test.route('/get_author', methods = ['GET'])
def get_test():
    authors = Author.query.all()
    content = '<p>Authors:</p>'
    for author in authors:
        content += '<p>%s</p>' % author.name
    return content


@mod_test.route('/new_author', methods = ['POST'])
def new_author():
    name = request.form['name']
    author = Author(name = name)
    author.save()
    return 'Saved :)'

@mod_test.route('/get_book', methods = ['GET'])
def get_book():
    book = Book.query.all()
    content = []
    for i in book:
        label = []
        author = []
        for a in i.label:
            label.append({
                'label' : a.label
            })
        for b in i.author:
            author.append({
                'name' : b.name
            })
        content.append({
            'title' : i.title,
            'year' : i.year,
            'author' : author,
            'label' : label
        })
    return jsonify(content)

@mod_test.route('/new_book', methods = ['POST'])
def new_book():
    title = request.form['title']
    year = request.form['year']
    author = request.form['author']
    label = request.form['label']
    author_a = Author.query.filter({'name':author}).all()
    label_a = Label.query.filter({'label': re.compile(label, re.IGNORECASE)}).all()
    a=''
    if author_a and label_a:
        book = Book(title = title, year=year, label = label_a, author=author_a)
        book.save()
        a = 'Saved'
    else:
        a='Author Atau Label Tidak Ada'

    return a
