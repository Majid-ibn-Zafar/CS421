from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import random
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Company(db.Model):
    __tablename__ = 'company'

    identification = db.Column(db.Integer, primary_key = True)
    companyname = db.Column(db.Text)
    email = db.Column(db.Text)
    phone = db.Column(db.Integer)
    address = db.Column(db.Text)

    def __init__(self, identification, companyname, email, phone, address):
        self.identification = identification
        self.companyname = companyname
        self.email = email
        self.phone = phone
        self.address = address

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userInput', methods = ['POST'])
def userInput():
    if request.method == 'POST':
        cID  = random.randint(1000000,9999999)
        cname = request.form.get('c')
        email = request.form.get('e')
        phone = request.form.get('p')
        address = request.form.get('a')

        newRecord = Company(cID, cname, email, phone, address)
        db.session.add(newRecord)
        db.session.commit()

        list_records = Company.query.all()

        return render_template('records.html', list_records = list_records)

    return render_template('records.html')

@app.route('/displayRecord', methods = ['POST', 'GET'])
def displayRecord():
    return render_template('records.html', list_records = Company.query.all())

@app.route('/deleteRecord', methods = ['POST', 'GET'])
def deleteRecord():
    if request.method == 'POST':
        companyid = request.form.get('d')

        Company.query.filter_by(identification = companyid).delete()
        db.session.commit()

    return render_template('records.html', list_records = Company.query.all())   

@app.route('/updateRecord', methods = ['POST', 'GET'])
def updateRecord():
    if request.method == 'POST':
        companyid = request.form.get('id')
        updated_cname = request.form.get('updated-c')
        updated_email = request.form.get('updated-e')
        updated_phone = request.form.get('updated-p')
        updated_address = request.form.get('updated-a')

        Company.query.filter_by(identification = companyid).update(dict(companyname = updated_cname, email = updated_email, phone = updated_phone, address = updated_address))
        db.session.commit()

    return render_template('records.html', list_records = Company.query.all())

if __name__ == "__main__":
    db.create_all()
    app.run()