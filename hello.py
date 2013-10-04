from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
import os

__author__ = 'Radostin'
from flask import Flask, url_for


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
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


user = User('test', 'test@test.com')
db.session.add(user)
db.session.commit()




@app.route("/")
def hello():
    #return redirect(url_for('static', filename='test.html'))
    return User.query.all()

if __name__ == "__main__":
    app.run()