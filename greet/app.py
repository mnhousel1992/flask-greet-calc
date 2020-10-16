from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return "<h1>welcome</h1>"


@app.route('/welcome/home')
def welcome_home():
    """add welcome home html"""
    return "<h1>Welcome home</h1>"


@app.route('/welcome/back')
def welcome_back():
    """Add welcome back html"""
    return "<h1>Welcome back</h1>"
