from flask_mail import Message
from .core import app, mail


def send_email(to, subject, template):
    mail.send(
        Message(subject=subject,
                recipients=[to],
                html=template,
                sender=app.config['MAIL_DEFAULT_SENDER']
                )
    )
