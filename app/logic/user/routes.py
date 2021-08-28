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

    #After login 
    if (login == True): 
        if(role == "teacher"):
            return render_template(
                'user/Tuserinfo.html',  
                data = login, 
                userinfo = userinfo,
                descripstion = 'load userinfo'
            )
        else:
            return render_template(
                'user/Suserinfo.html',  
                data = login, 
                userinfo = userinfo,
                descripstion = 'load userinfo'
            )

    else:
        return redirect(url_for('login.login_main'))