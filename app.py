#!/usr/bin/env pyhton3

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# Define the Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    message = db.Column(db.Text)

# Create the database tables
with app.app_context():
    db.create_all()


@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/contact', methods=['GET', 'POST'], strict_slashes=False)
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        new_contact = Contact(name=name, email=email, phone=phone, message=message)

        db.session.add(new_contact)
        db.session.commit()

        return redirect(url_for('thank_you'))

    return render_template('contact.html')


@app.route('/thank_you')
def thank_you():
    return "Thank you for contacting us!"
    return render_template('contact.html')


@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')


@app.route('/skills', strict_slashes=False)
def skills():
    return render_template('skills.html')


if __name__ == '__main__':
    app.run(debug=True)
