from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/test')
def test():
    return render_template('test.html')
