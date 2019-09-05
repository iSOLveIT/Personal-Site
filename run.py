from pkg import app
import os

if __name__ == '__main__':
    app.secret_key = os.urandom(75)
    app.run(host='0.0.0.0',port=5000, debug=True)