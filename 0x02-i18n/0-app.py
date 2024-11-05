#!/usr/bin/env python3
""" The flak app """
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    """
    this funtion simply output a text
    """
    return render_template('0-index.html')


if __name__ == '__name__':
    app.run()
