from flask import Flask
from datebase.database import db
from flask_migrate import Migrate
from flask import Flask
from flask_login import LoginManager
import secrets


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/python/site/instance/database.db'
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
