#!/usr/bin/env python3
"""A basic flask app"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config_class.from_object('Config')
babel = Babel(app)


@app.route('/')
def get_page() -> str:
    """The home page route"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
