#!/usr/bin/env python3
"""
Welcome to Holberton
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    languages config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
     Return best match from accepted languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])



@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello world
    """
    return render_template('2-index.html')