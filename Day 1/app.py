from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return "I am Shuaib and I am learning Flask for web development."


@app.route('/about')
def about():
    return "This is the about page of the Flask application."

@app.route('/contact')
def contact():
    return "This is the contact page of the Flask application."


@app.route('/services')
def services():
    return "This is the services page of the Flask application."

@app.route('/hello')
def hello():
    return "Hello, welcome to my Flask application!"


@app.route('/user/<name>')
def user(name):
    return f"Hello {name}, Welcome to flask!"

if __name__ == '__main__':
    app.run(debug=True, port=8000)