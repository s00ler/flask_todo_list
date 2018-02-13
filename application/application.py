from flask import flash, redirect, render_template, url_for

from .core import app, database
from .email import send_email
from .forms import AddTaskForm, LoginForm, RegisterForm
from .models import User
from .token import confirm_token, generate_confirmation_token


@app.route('/')
def hello():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    else:
        return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User(email=email, password=password)
        database.add(user)
        database.sessiom.commit()
        token = generate_confirmation_token(user.email)
        confirm_url = url_for('user.confirm_email',
                              token=token, _external=True)
        html = render_template('activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)
    else:
        return render_template('register.html', form=form)


# @app.route('/confirm/<token>')
# @login_required
# def confirm_email(token):
#     pass
