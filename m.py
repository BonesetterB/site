from app import app
from database import db
from Modules import User

username='Mike'
email='camurau1992@gmail.com'
with app.app_context():
    if User.query.filter_by(username=username).first():
                    print('Username already exists')

    if User.query.filter_by(email=email).first():
        print('Email already registered')