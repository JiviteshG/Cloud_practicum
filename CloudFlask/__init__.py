"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)

import CloudFlask.views
