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
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages
    """
    return request.accept_languages

@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello world
    """
    return render_template('0-index.html')


