"""
This file is dedicated to the Views.
Is maps the request to the correct view.
"""


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    """
    Renders the hello world test page.
    """
    return render_template("home.html")


@app.route("/base")
def base():
    """
    This method renders the base tempaplate.

    :return: html page
    """
    return render_template("base.html")


@app.route("/developer")
def developer():
    """
    This method renders the develper page, which
    is dedicated to introducing the "developer Marcus".

    :return: html page
    """
    return render_template("developer.html")


@app.route("/resume")
def resume():
    """
    This method renders the resume page, which will
    render an html version of my resume.

    :return: html page
    """
    return render_template("resume.html")


@app.route("/chinese")
def chinese():
    """
    This method renders the chinese page, which will be dedicated
    to giving me an outlet to host chinese related things.

    :return: html page
    """
    return render_template("chinese.html")

@app.route("/friends")
def friends():
    """
    This method renders the friends page, which will be dedicated
    to thanking my friends for their help.

    :return: html page
    """
    return render_template("friends.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
