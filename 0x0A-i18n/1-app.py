#!/usr/bin/env python3
"""
Welcome to Holberton
"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    languages, locale, timezone
    """
    LANGUAGES = ['en', 'fr']
    Babel_default_locale = 'en'
    Babel_default_timezone = 'UTC'


@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello world
    """
    return render_template('0-index.html')
