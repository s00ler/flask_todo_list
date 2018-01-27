from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, Label
from wtforms.validators import Email, DataRequired


class LoginForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[Email(), DataRequired()])

    password = PasswordField(label='Password', validators=[DataRequired()])
    signin = SubmitField(label='Sign in')
    signup = SubmitField(label='Sign up')


class TaskForm(FlaskForm):
    def __init__(self, text, id):
        self.name = Label(text=text)
        self.done = SubmitField(label='Done!')
