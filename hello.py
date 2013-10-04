import random
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
import os

__author__ = 'Radostin'
from flask import Flask, url_for


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/testcomm'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name

@app.route("/")
def hello():
    user = User('test' + str(random.random()), 'test@test.com')
    db.session.add(user)
    db.session.commit()

    #return redirect(url_for('static', filename='test.html'))
    return str(User.query.all())

if __name__ == "__main__":
    app.run()