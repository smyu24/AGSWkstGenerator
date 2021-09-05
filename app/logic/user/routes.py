"""Route declaration."""
#system imports
from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from app import db

user_dp = Blueprint('user',__name__, url_prefix='/user', template_folder='templates',static_folder='static')

class userinfo(FlaskForm):
    username = StringField('username') 
    role = StringField('role')

@user_dp.route('/')
def main_user():
    login = False
    if 'response' in session:
        login = True
        userinfo = session['response']
        role = str(session['role'])[2:9]

    #Example define Should get this from the SQL
    lt = [] #learning target

    lt.append("6") #number of the lt

    lt.append("Pre-Algebra") #title
    lt.append("a course designed to prepare students for a standard high school algebraic course.") #desc

    lt.append("Algebra 1") #title
    lt.append("a course designed to prepare students for a standard high school algebraic course.") #desc

    lt.append("AGS 1") #title
    lt.append("a course designed to prepare students for a standard high school algebraic course.") #desc

    lt.append("Geometry") #title
    lt.append("a course designed to prepare students for a standard high school algebraic course.") #desc

    lt.append("Algebra 2") #title
    lt.append("a course designed to prepare students for a standard high school algebraic course.") #desc

    lt.append("Pre-Calculus") #title
    lt.append("a course designed to prepare students for a standard high school algebraic course.") #desc

    #After login 
    if (login == True): 
        print(role)
        if(role == "teacher"):
            return render_template( #teacher
                'user/Tuserinfo.html',  
                data = login, userinfo = userinfo, descripstion = 'load userinfo'
            )
        elif(role == "student"):
            return render_template( #student
                'user/Suserinfo.html',  
                data = login, userinfo = userinfo, descripstion = 'load userinfo'
            )
        else:
            return render_template( #parents
                'user/Puserinfo.html',  
                data = login, userinfo = userinfo, descripstion = 'load userinfo', lt = lt
            )
    else:
        return redirect(url_for('login.login_main'))