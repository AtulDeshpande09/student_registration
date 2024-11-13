from flask import Flask, render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import LoginManager

from models import db
from config import Config
# configure app
app = Flask(__name__)

app.config.from_object(Config)

# initiate db
db.init_app(app)

with app.app_context():
    db.create_all()

# initiate login manager
login_manager = LoginManager(app)



@app.route('/')
def dash():
    return render_template('dashboard.html')

#from query import add_student

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    from models import Student
    from query import add_student
    if request.method=='POST':
        response = request.form
        
        name = response['name']
        email = response['email']
        course = response['course']
        password = response['password']
        
        # Add it to database
        add_student(name,email,course,password)

        return "Student Registered Successfully!"
    
    return render_template('register.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email = request.form['Email']
        password = request.form['Password']
        
        #created temporary dict to handle error
        database= {}

        if email in database[email]:
            # modify this later
            login = True if database[password]==password else False

    return render_template('login.html')


if __name__ == '__main__':
    app.run()    
