# Third-party modules 
from flask import Flask
from flask_mail import Mail
# Built-in modules 
import os


app = Flask(__name__)   # Initialize Flask

# Configure Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = str(os.environ.get('MAIL_USERNAME'))
app.config['MAIL_PASSWORD'] = str(os.environ.get('MAIL_PASSWORD'))
app.config['MAIL_MAX_EMAILS'] = 1000

mail = Mail(app)    # Instantiate Mail into app

from pkg import routes
