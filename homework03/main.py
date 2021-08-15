import os
import sqlite3
import random
import string
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

baseDirectory = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDirectory, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'

    identification = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    grade = db.Column(db.Integer)

    def __init__(self, identification, name, grade):
        self.identification = identification
        self.name = name
        self.grade = grade

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enteredCredentials', methods = ['POST', 'GET'])
def enteredCredentials():
    if request.method == 'POST':
        student_identification_number  = random.randint(1000000,9999999)
        name_of_student = request.form.get('Name of Student')
        grade_of_student = request.form.get('Final Grade Results')

        newEntry = Student(student_identification_number, name_of_student, grade_of_student)
        db.session.add(newEntry)
        db.session.commit()

        list_students = Student.query.all()

        return render_template('results.html', list_students = list_students)

    return render_template('results.html')

@app.route('/credentialDeletion',methods = ['POST', 'GET'])
def credentialDeletion():
    if request.method == 'POST':
        student_id = request.form.get('random identification Number')
        Student.query.filter_by(identification = student_id).delete()
        db.session.commit()

    return render_template('results.html', list_students = Student.query.all())

@app.route('/resultDisplay')
def resultDisplay():
    return render_template('results.html', list_students = Student.query.all())

@app.route('/resultDisplay2')
def resultDisplay2():
    return render_template('results.html', list_students = Student.query.filter(Student.grade>=85))


if __name__ == "__main__":
    db.create_all()
    app.run()
