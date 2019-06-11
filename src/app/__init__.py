# -*- encoding: utf-8 -*-
"""
Simple Flask Application 
Coded for https://docs.appseed.us/tutorials/flask-learn-by-coding/
Author: AppSeed.us
License: MIT
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, your Up!'

@app.route('/')
def index():
    return render_template( 'layouts/default.html',
                            title='Flask - Learn by Coding',
                            description='Simple Flask tutorial for beginners.',
                            content=render_template('pages/index.html') ) 
