from datebase.database import db
from sqlalchemy import Column, JSON, Integer, String
from flask_login import UserMixin
from app import login_manager

class User(UserMixin,db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Game(UserMixin,db.Model):
    id = Column(Integer, primary_key=True)
    img = Column(String(500), unique=True, nullable=True)
    name = Column(String(150), unique=True, nullable=True)
    companies = Column(JSON,unique=False, )
    platforms = Column(JSON, unique=False, nullable=True)
    date = Column(String(100), unique=False, nullable=True)

    def __repr__(self):
        return f'<Game {self.name}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))