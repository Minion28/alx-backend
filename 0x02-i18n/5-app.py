#!/usr/bin/env python3
'''
mock logging in
'''

from typing import Union
from flask import Flask, render_template, request, g
from os import getenv
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"g": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"g": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"g": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"g": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    ''' app Config '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('5-app.Config')


@app.before_request
def before_request():
    '''
    check if user is available'''
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    '''
    Determine best match with supported languages
    '''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    '''
    return 5-index.html
    '''
    return render_template('5-index.html')


def get_user() -> Union[dict, None]:
    '''
    Returns a user
    '''
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
