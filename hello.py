from werkzeug.utils import redirect

__author__ = 'Radostin'
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return redirect(url_for('static', filename='test.html'))

if __name__ == "__main__":
    app.run()