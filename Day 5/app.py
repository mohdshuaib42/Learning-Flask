from flask import Flask, make_response, session, sessions, request, url_for, redirect

app = Flask(__name__)

session['user'] = "shuaib"
session['login_time'] = "10:30 AM"

@app.route('/setcookie')
def setcookie():
    res = make_response("Cookie Set")
    res.set_cookie('name', 'shuaib')
    return res

@app.route('/getcookie')
def getcookie():
    return request.cookies.get('name')



def is_logged_in():
    return 'user' in session

@app.route('/dashboard')
def dashboard():
    if not is_logged_in():
        return redirect(url_for('login'))
    return "Dashboard"