"""Route declaration."""
from flask import Blueprint, redirect, render_template, url_for, request, session, make_response, abort, flash
from .forms import ContactForm, SignupForm
from datetime import timedelta
from flask_login import current_user, UserMixin, login_required, login_user, logout_user
from app import db
from werkzeug.security import check_password_hash, generate_password_hash


"""class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    classrooms = db.Column(db.Text)
    parent = db.Column(db.Text)
    worksheets = db.Column(db.Text)
    ADHD = db.Column(db.Boolean)"""


# Blueprint Configuration
home_bp = Blueprint('home', __name__, url_prefix='/', template_folder='templates',static_folder='static') # first argument is the blueprints name,second argument is very important it’s the import_name,The third argument is the url prefix of the blueprint
"""
nav = [
    {'name': 'Home', 'url': '/'},
    {'name': 'Prealgebra', 'url': '/prealgebra'},
    {'name': 'AGS1', 'url': '/AGS1'},
    {'name': 'test', 'url': '/test'}
]
"""
"""
    login_manager.login_view = 'user.login'

has an is_authenticated() method that returns True if the user has provided valid credentials
has an is_active() method that returns True if the user’s account is active
has an is_anonymous() method that returns True if the current user is an anonymous user
has a get_id() method which, given a User instance, returns the unique ID for that object
"""

"""
@home_bp.before_request
def before_request():
    if login_manager.is_authenticated and request.endpoint != 'login':
        return redirect(url_for('login'))

@home_bp.before_request
def makesession_permanent():
    session.permanent = True
    home_bp.permanent_session_lifetime = timedelta(minutes = 90)
"""

"""
@login_manager.user_loader
def load_user(userid):
    try:
        #: Flask Peewee used here to return the user object
        #return User.get(User.id==userid)
        return
    except:
        return None

@home_bp.route('/login', methods=["GET", 'POST'])
def login():

    if request.method == "POST":
        if not request.form.get("username"):
            abort(403, 'Must Provide An Username')
        elif not request.form.get("email"):
            abort(403, 'Must Provide An Email')
        elif not request.form.get("password"):
            abort(403, 'Must Provide A Password')
        elif not request.form.get("confirmation"):
            abort(403, 'Must Provide A Password Confirmation')
        #elif not request.form.get("roles"):
            #abort(403, 'Must Provide A Role') # not a form

        # Query database for username
        rows = db.connection.cursor()
        rows.execute('SELECT * from Users WHERE username = :username',
                            username = request.form.get("username"))
        user_data = str(rows.fetchone())

        # Ensure username exists and password is correct
        if len(user_data) != 1 or not check_password_hash(user_data[0]["hash"], request.form.get("password")):
            abort(400, 'Invalid Username and/or Password')

        login_user(user_data[0]["id"]) # Remember which user has logged in
        flash("Logged In")
        return redirect("/") # Redirect user to home page

    else: # "GET" method
        return render_template(
        'login.html',
        title='Login',
        subtitle='Math Worksheet Generator'
        )
"""

"""    agent = flask_login.current_user
    # https://flask-login.readthedocs.org/en/latest/#anonymous-users
    is_logged_in = agent.get_id() is not None"""


@home_bp.route('/login', methods=["GET", 'POST'])
def login():
    return render_template(
    'login.html',
    title='Login',
    subtitle='Math Worksheet Generator'
    )

@home_bp.route('/')
#@login_required
def index():
    #login = current_user
    #if load_user(login) != None:
        #login = True
    login = False
    return render_template(
        'index.html',
        data = login,
        title='Math Worksheet Generator',
        subtitle='Math Worksheet Generator'
    )


@home_bp.route('/signup')
def signup():

    return render_template(
        'register.html',
        title='Signup',
        subtitle='Math Worksheet Generator'
    )


@home_bp.route('/logout')
def logout():
    #logout_user()
    return redirect(url_for('home.login')) # redirect("/login")
'''
#check sign up forms
@home_bp.route('/signup', methods=['GET', 'POST'])
def signup_page():
    """User sign-up page."""
    signup_form = SignupForm(request.form)
    # POST: Sign user in
    if request.method == 'POST':
        if signup_form.validate():
            # Get Form Fields
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            website = request.form.get('website')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(
                    name=name,
                    email=email,
                    password=generate_password_hash(
                        password,
                        method='sha256'
                    ),
                    website=website
                )
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('home'))
            flash('A user exists with that email address.')
            return redirect(url_for('auth_bp.signup_page'))
    # GET: Serve Sign-up page
    return render_template(
        '/signup.html',
        title='Create an Account',
        form=SignupForm(),
        template='signup-page', # not generated yet
        body="Sign up for a user account."
    )
'''

"""
@home_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.html",
        form=form,
        template="form-template"
    )"""

#Securely Redirect Back
"""
@app.errorhandler(404)
def page_not_found():
    return make_response(render_template('pages/404.html'), 404)

@app.errorhandler(405)
def bad_request():
    return make_response(render_template('pages/405.html'), 405)

@home_bp.errorhandler(500)
def server_error():
    return make_response(render_template("500.html"),500)
"""
