from flask import Flask
from flask_mail import Mail


app = Flask(__name__)

# EMAIL DETAILS
_mail_log = {'e-mail':'isolveitgroup@gmail.com', 'pswd':'laden@1472'}

# Config Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = _mail_log['e-mail']
app.config['MAIL_PASSWORD'] = _mail_log['pswd']
app.config['MAIL_MAX_EMAILS'] = None

mail = Mail(app)


from pkg import routes