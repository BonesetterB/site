from flask import Blueprint,render_template, request,redirect
from database import db
from Modules import User

home=Blueprint('home',"home")


@home.route('/')
def base():
    return render_template('home.html')

@home.route('/Forum')
def Forum():
    return render_template('Forum.html')

@home.route('/Forums')
def Forums():
    return render_template('Forums.html')

@home.route('/Game')
def Game():
    return render_template('Game.html')

@home.route('/Games')
def Games():
    return render_template('Games.html')

@home.route("/Log", methods=['GET', 'POST'])
def Log():
    username_error=''
    password_error=''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not User.query.filter_by(username=username).first():
            username_error='User don`t exsist'

        if not User.query.filter_by(password=password).first():
            password_error='Incorect password'

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            return f'Welcome, {user.username}!'

    return render_template('Log.html',username_error=username_error, password_error=password_error)

@home.route('/New')
def New():
    return render_template('New.html')

@home.route('/News')
def News():
    return render_template('News.html')

@home.route('/Sign', methods=['GET', 'POST'])
def Sign():
    error_username = ''
    error_password = ''
    error_email=''
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if User.query.filter_by(username=username).first():
            error_username = 'Username already exists'

        if password != confirm_password:
            error_password = 'Passwords do not match'
        if User.query.filter_by(email=email).first():
            error_email='This email already exists'

        if not error_username and not error_password and not error_email:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            return redirect('/Log')

    return render_template('Sign.html', error_username=error_username, error_password=error_password,error_email=error_email)