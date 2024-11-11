from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):

    id = db.Column(db.Integer , primary_key=True)

    name = db.Column(db.String(50),nullable=False)

    email = db.Column(db.String(50), unique=True , nullable=False)

    gender = db.Column(db.String(1),nullable=True)

    course = db.Column(db.String(20),nullable=True)

    password = db.Column(db.String(100) , nullable=False)
