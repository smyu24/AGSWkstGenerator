"""Route declaration."""
#system imports
from flask import Blueprint, render_template
algebra_bp = Blueprint('algebra',__name__, url_prefix='/algebra', template_folder='templates',static_folder='static')

#nav List
nav = [
    {'name': 'Home', 'url': '/'},
    {'name': 'Prealgebra', 'url': '/prealgebra'},
    {'name': 'Algebra', 'url': '/algebra'},
    {'name': 'Load', 'url': '/loadwkst'},
    {'name': 'Contact', 'url': '/contact'}
    #{'name': 'Signup', 'url': '/signup'}
]

@algebra_bp.route('/')
def algebra_main():
    #passing dict to contruct 

    return render_template(
        'algebra/algebra.html', 
        nav=nav , 
        descripstion = 'algebra/01'
        )