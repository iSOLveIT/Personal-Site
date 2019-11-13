from flask import Flask
from flask_mail import Mail


app = Flask(__name__)

# EMAIL DETAILS
_mail_log = {'e-mail':'isolveitgroup@gmail.com', 'pswd':'enbmokslplqokjed'}

# Config Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = _mail_log['e-mail']
app.config['MAIL_PASSWORD'] = _mail_log['pswd']
app.config['MAIL_MAX_EMAILS'] = 1000

mail = Mail(app)


from pkg import routes