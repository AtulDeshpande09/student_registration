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



# import routes , models and forms

#from models import Student
from forms import RegistrationForm , LoginForm

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
        
        #Store Data in variable temporarily
        name = form.name.data
        email = form.email.data
        gender = form.gender.data
        #course = request.form['Course']
        password = form.password.data
        
        # Add it to database
        add_student(name,email,gender,password)

        flash('Student Registered Successfully','success')

        return redirect(url_for('dashboard.html'))
    
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
