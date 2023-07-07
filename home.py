from flask import Blueprint

home=Blueprint('home')

@home.route('/')
def hone():
    return 'Home page'