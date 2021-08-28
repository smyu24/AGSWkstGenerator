"""Route declaration."""
#system imports
from flask import *
from flask_mysqldb import MySQL, MySQLdb
from app import db
from datetime import timedelta
import bcrypt
import MySQLdb
import uuid


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

@login_bp.before_request
def makesession_permanent():
    session.permanent = True
    login_bp.permanent_session_lifetime = timedelta(minutes = 60)

@login_bp.route('/', methods=["GET", "POST"])
def login_main():
    #passing dict to contruct 
    login = False
    if 'response' in session:
        login = True

    if (login == False):
        if request.method == 'GET': 
            return render_template(
                'login/login.html', 
                nav=nav , 
                descripstion = 'login'
            )
        
        else:
            email = request.form['email']
            password = request.form['password']
            cur = db.connection.cursor()
            
            #Where collect all data
            cur.execute('SELECT * from accounts where email = %s AND password = %s', (email, password))
            data = cur.fetchone()

            #where collect the role of the user
            cur.execute('SELECT role from accounts where email = %s AND password = %s', (email, password))
            role = cur.fetchone()

            cur.close()

            if data is None:
                return 'Failed'
            else:
                session['response'] = data
                session['role'] = role
            
                return redirect(url_for('home.index'))
    else:
        return redirect(url_for('home.index'))


@login_bp.route('/mmtsignup', methods=["GET", "POST"])
def signup():
    login = False
    if 'response' in session:
        login = True

    if (login == False):
        if request.method == 'GET':
            return render_template(
                'login/signup.html',
                nav=nav,
                descripstion = 'Sign Up'
            )
        else:
            uid = uuid.uuid1()
            name = request.form['name']
            Fname = request.form['Fname']
            Lname = request.form['Lname']
            email = request.form['email']
            pswd = request.form['password']
            role = request.form['roles']

            cur = db.connection.cursor()
            cur.execute("INSERT INTO accounts(uid, username, Fname, Lname, email, password, role) VALUES(%s, %s, %s, %s, %s, %s, %s)", (uid, name, Fname, Lname, email, pswd, role))
            db.connection.commit()
            cur.close()
        
            return redirect(url_for('login.login_main'))
    else:
        return redirect(url_for('home.index'))