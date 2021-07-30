"""Route declaration."""
#system imports
from flask import Blueprint, render_template, request
#from .prealgebraforms import DecimalPlace
from app import db
from .decimal_place import Decimal_Places
prealgebra_bp = Blueprint('prealgebra',__name__, url_prefix='/prealgebra', template_folder='templates',static_folder='static')

#nav List
nav = [
    {'name': 'Home', 'url': '/'},
    {'name': 'Prealgebra', 'url': '/prealgebra'},
    {'name': 'Algebra', 'url': '/algebra'},
    {'name': 'Load', 'url': '/loadwkst'},
    {'name': 'Contact', 'url': '/contact'}
    #{'name': 'Signup', 'url': '/signup'}
]

@prealgebra_bp.route('/')
def prealgebra_main():
    return render_template(
        'prealgebra/prealgebra.html', 
        nav=nav , 
        descripstion = 'prealgebra/01'
        )

@prealgebra_bp.route('/1-1-1', methods=["GET", "POST"])
def prealgebra_sec1():
    if request.method == 'GET':
        return render_template(
            'prealgebra/prealgebra.html', 
            seed = '1-1-1',
            nav=nav , 
            descripstion = 'prealgebra/01'
        )
    else:
        sname = request.form['studnetName']
        tname = "aiden O."
        seed = request.form['master']
        title = request.form['pdftitle']
        desc = request.form['pdfdesc']
        master = str(Decimal_Places(seed))
    
    #custom function
        cur = db.connection.cursor()
        cur.execute("INSERT INTO mmtseed VALUES(%s, %s, %s, %s, %s)", (title, desc, sname, tname, master))
        db.connection.commit()
        cur.close()
        return render_template(
            'prealgebra/prealgebra.html', 
            seed = '1-1-1',
            nav=nav , 
            descripstion = 'prealgebra/01'
        )


@prealgebra_bp.route('/01_decimal_place')
def decimal_place():

    return render_template('prealgebra/01_decimal_place.html')

@prealgebra_bp.route('/02_decimal_place')
def reading_writing():

    return render_template('prealgebra/02_naming.html')