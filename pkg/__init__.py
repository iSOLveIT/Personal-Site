# Third-party modules 
from flask import Flask, request
from flask_mail import Mail
from flask_compress import Compress
# Built-in modules 
import os
# import ssl

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

# Configure Flask Compress
app.config['COMPRESS_MIMETYPES'] = ['text/html','text/css', 'text/javascript', 'application/javascript',
                                    'application/json', 'application/vnd.ms-fontobject', 
                                    'image/svg+xml','font/ttf', 'font/woff', 'font/woff2']

Compress(app)       # Instantiate Compress into app

# Security measures
@app.after_request
def apply_headers(response):
    compression = request.headers["Accept-Encoding"]
    algorithm = x if (x:='br') in compression else 'gzip'
    app.config['COMPRESS_ALGORITHM'] = algorithm    # configure compress algorithm

    response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubdomains; preload"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Cache-Control"] = "max-age=10368000"      # 4 months

    return response


from pkg import routes
