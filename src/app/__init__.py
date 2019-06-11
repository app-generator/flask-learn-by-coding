# -*- encoding: utf-8 -*-
"""
Simple Flask Application 
Coded for https://docs.appseed.us/tutorials/flask-learn-by-coding/
Author: AppSeed.us
License: MIT
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, your Up!'
