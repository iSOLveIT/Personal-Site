from pkg import app
import os

app.config['SECRET_KEY'] = os.urandom(75)

if __name__ == '__main__':
    app.run()
