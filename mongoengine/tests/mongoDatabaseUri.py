import os
from flask import Flask
import unittest
import tempfile

class MongoDatabaseUri(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['MONGOALCHEMY_DATABASE'] = 'testMongo'
        self.app.config['TESTING'] = True
        self.db = mongoalchemy.MongoAlchemy(self.app)
        self.Todo = _make_todo_document(self.db)

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['MONGOALCHEMY_DATABASE'])

if __name__ == '__main__':
    unittest.main()
