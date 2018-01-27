from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('email', validators=[Email(), DataRequired])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')
