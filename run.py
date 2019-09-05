from pkg import app
import secrets

app.config['SECRET_KEY'] = secrets.token_hex(75)

if __name__ == '__main__':
    app.run()