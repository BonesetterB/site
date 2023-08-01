from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/python/site/instance/database.db'
db.init_app(app)