"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/projectdb'
heroku = Heroku(app)
db = SQLAlchemy(app)

import CloudFlask.views
