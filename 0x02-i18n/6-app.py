#!/usr/bin/env python3
'''
user locale
'''

from typing import Union
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    '''
    config class
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('6-app.Config')


@app.before_request
def before_request():
    '''
    Function before request
    '''
    g.user = get_user()


@babel.localeselector
def get_locale():
    '''
    Determine best match with supported languages
    '''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    '''
    return 6-index.html
    '''
    return render_template('6-index.html')


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
