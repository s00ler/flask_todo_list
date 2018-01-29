from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, Label
from wtforms.validators import Email, DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[Email(), DataRequired()])

    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class RegisterForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[Email(), DataRequired()])

    password = PasswordField(label='Password', validators=[
                             DataRequired(),
                             EqualTo('confirm')])
    confirm = PasswordField(label='Confirm')
    submit = SubmitField(label='Sign up')


class AddTaskForm(FlaskForm):
    description = StringField(label='New task', validators=[DataRequired()])
    submit = SubmitField(label='Add')


class TaskForm
