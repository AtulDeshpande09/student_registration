from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField
from wtforms.validators import DataRequired , Email , Length

class RegistrationForm:

    name = StringField('Name',validators=[])
    email = StringField('Email',validators=[])

    password = PasswordField('Password', validators=[])

    submit = SubmitField('Register')


class LoginForm:

    email = StringField('Email',validators=[])

    password = PasswordField('Password', validators=[])

    submit = SubmitField('Register')
