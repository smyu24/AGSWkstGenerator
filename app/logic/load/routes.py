"""Route declaration."""
#system imports
from flask import Blueprint, render_template, request
from app import db
load_dp = Blueprint('load',__name__, url_prefix='/load', template_folder='templates',static_folder='static')

#nav List
nav = [
    {'name': 'Home', 'url': '/'},
    {'name': 'Prealgebra', 'url': '/prealgebra'},
    {'name': 'Algebra', 'url': '/algebra'},
    {'name': 'Load', 'url': '/loadwkst'},
    {'name': 'Contact', 'url': '/contact'}
    #{'name': 'Signup', 'url': '/signup'}
]

@load_dp.route('/')
def load_main():
    cur = db.connection.cursor()
    cur.execute("SELECT title FROM mmtseed WHERE sname LIKE 'jaegeun'")
    title = cur.fetchall()

    #cur.execute("SELECT desc FROM mmtseed WHERE sname LIKE 'jaegeun'")
    #desc = cur.fetchall()

    cur.execute("SELECT sname FROM mmtseed WHERE sname LIKE 'jaegeun'")
    sname = cur.fetchall()

    cur.execute("SELECT tname FROM mmtseed WHERE sname LIKE 'jaegeun'")
    tname = cur.fetchall()

    cur.execute("SELECT seed FROM mmtseed WHERE sname LIKE 'jaegeun'")
    seed = cur.fetchall()

    arr = [title, sname, tname, seed]
    print(arr)

    return render_template(
        'load/load.html',  
        descripstion = 'load worksheet',
        darr = arr
        )