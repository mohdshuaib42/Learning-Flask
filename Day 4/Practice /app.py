from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "secret123"

@app.route('/start')
def home():
    return render_template('index.html', name="Shuaib" )

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', username="Shuaib")

@app.route('/about')
def about():
    return "This is the About page"

@app.route('/contact')
def contact():
    return "This is the Contact page"

@app.route('/services')
def services():
    return "This is the Services page"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "Shuaib":
            return redirect(url_for('dashboard'))
        
        else:
            flash("Invalid User")
            return redirect(url_for('login'))
    
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)
