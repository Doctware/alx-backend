#!/usr/bin/env python3
""" The flak app """
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Optional

app = Flask(__name__)


class Config:
    """ the config class for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_local() -> Optional[str]:
    """ this function determin the best mach with supported language """
    return request.accpt_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    this funtion simply output a text
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
