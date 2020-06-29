# Local modules 
from pkg import app
# Built-in modules 
import os

app.config['SECRET_KEY'] = str(os.environ.get('SECRET_KEY'))   #Secret key

if __name__ == '__main__':
    app.run(threaded=True) # ssl_context='adhoc'  # threaded - launches a new thread on each request
