from crypt import methods
from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
    
@auth.route('/sign-up', methods=['GET', 'POST'])
def sing_up():
    
    return render_template("sign_up.html")

