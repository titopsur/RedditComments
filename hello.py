from werkzeug.utils import redirect
from flask.ext.sqlalchemy import SQLAlchemy
import os

__author__ = 'Radostin'
from flask import Flask, url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return redirect(url_for('static', filename='test.html'))

if __name__ == "__main__":
    app.run()