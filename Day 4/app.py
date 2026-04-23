from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

app.secret_key = "secret123"

@app.route('/')
def home():
    return "Home Page"

@app.route('/go')
def go():
    return redirect(url_for('home'))

@app.route('/user/<name>')
def user(name):
    return f"Hello {name}"

@app.route('/login')
def login():
    return redirect(url_for('user', name="Shuaib"))