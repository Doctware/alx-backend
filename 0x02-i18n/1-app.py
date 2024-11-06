#!/usr/bin/env python3
""" The flak app """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ the config class for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABE_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
    this funtion simply output a text
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
