from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "secret123"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        return redirect(url_for('dashboard'))
    else:
        flash("Invalid User")
        return redirect(url_for('login'))
    
    return render_template('login.html')