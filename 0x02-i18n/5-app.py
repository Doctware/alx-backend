#!/usr/bin/env python3
""" The flak app """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional

app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ the config class for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_user() -> dict | None:
    """ this function get a user of exists """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """ set g.user to the user foubd by get_user, else retur none """
    g.user = get_user()


@babel.localeselector
def get_locale() -> Optional[str]:
    """ this function determin the best mach with supported language """

    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user.get("locale") in app.config['LANGUAGES']:
        return g.user["locale"]

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    this funtion simply output a text
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
