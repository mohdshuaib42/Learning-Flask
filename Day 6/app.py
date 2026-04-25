from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()

    if Student.query.count() == 0:
        student1 = Student(name="Shuaib", course="Flask")
        student2 = Student(name="Ayesha", course="Python")

        db.session.add(student1)
        db.session.add(student2)
        db.session.commit()


@app.route("/")
def home():
    return "Home Page"


@app.route("/users")
def users():
    students = Student.query.all()

    output = ""
    for student in students:
        output += f"ID: {student.id}, Name: {student.name}, Course: {student.course}<br>"

    return output


if __name__ == "__main__":
    app.run(debug=True)
