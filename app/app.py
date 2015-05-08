"""
This file is dedicated to the Views.
Is maps the request to the correct view.
"""


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

@app.route("/home")
def home():
    return render_template("index.html")
