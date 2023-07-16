from flask import Flask
from database import db
from flask_migrate import Migrate
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
login_manager = LoginManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/python/site/instance/database.db'
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
