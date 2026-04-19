from flask import Flask, render_template 
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/student/<name>')
def student(name):
    return render_template("student.html",username=name)

@app.route('/about')
def about():
    
    return render_template('about.html',sname="Shuaib",course="Flask",year = datetime.now().year)
app.run()