# Local modules 
from pkg import app
# Built-in modules 
import os

app.config['SECRET_KEY'] = os.urandom(75)   #Secret key

if __name__ == '__main__':
    app.run(debug=True, threaded=True)  # threaded - launches a new thread on each request
