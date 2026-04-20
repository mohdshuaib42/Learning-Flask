from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        city = request.form['city']
        return render_template('add.html', city=city)
    return render_template('add1.html')
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)