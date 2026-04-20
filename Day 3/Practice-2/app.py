from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/add', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return render_template('result.html', username=username, password=password)
    return render_template('form.html')
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)