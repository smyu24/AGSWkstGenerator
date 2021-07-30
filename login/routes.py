"""Route declaration."""
#system imports
from flask import Blueprint, render_template, request
from flask_mysqldb import MySQL, MySQLdb
from app import db
import bcrypt
import MySQLdb



login_bp = Blueprint('login',__name__, url_prefix='/login', template_folder='templates',static_folder='static')

#nav List
nav = [
    {'name': 'Home', 'url': '/'},
    {'name': 'Prealgebra', 'url': '/prealgebra'},
    {'name': 'Algebra', 'url': '/algebra'},
    {'name': 'Load', 'url': '/loadwkst'},
    {'name': 'Contact', 'url': '/contact'}
    #{'name': 'Signup', 'url': '/signup'}
]

@login_bp.route('/')
def login_main():
    #passing dict to contruct 
    return render_template(
        'login/login.html', 
        nav=nav , 
        descripstion = 'login'
    )

@login_bp.route('/mmtsignup', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        return render_template(
            'login/signup.html',
            nav=nav,
            descripstion = 'Sign Up'
        )
    else:
        name = request.form['name']
        email = request.form['email']
        cur = db.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        db.connection.commit()
        cur.close()
        return 'success'

        return render_template('index.html')

@login_bp.route('/lookup', methods=["GET"])
def search():
    if request.method == 'GET':
        cur = db.connection.cursor()
        cur.execute('SELECT * FROM users')
        select = list(cur.fetchall())

        print(select)

        return 'success'

#    return render_template(
#        'login/signup.html',
#        nav=nav,
#        descripstion = 'Sign Up'
#    )