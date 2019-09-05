from flask import Flask
from flask_mail import Mail


app = Flask(__name__)


# Config Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'email_address'
app.config['MAIL_PASSWORD'] = 'email_password'
app.config['MAIL_MAX_EMAILS'] = None

mail = Mail(app)


from pkg import routes