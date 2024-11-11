from models import Student
from app import db

def add_student(name,email,gender,password):

    new_student = Student(name=name,email=email,gender=gender,password=password)

    db.session.add(new_student)
    db.session.commit()


