"""Route declaration."""
#system imports
from flask import Blueprint, render_template , request , make_response  
from .forms import ContactForm, SignupForm

# Blueprint Configuration
home_bp = Blueprint(
    'home', __name__,
    template_folder='templates',
    static_folder='static'
)

#top basic nav bar options
nav = [
    {'name': 'Home', 'url': '/'},
    {'name': 'Prealgebra', 'url': '/prealgebra'},
    {'name': 'Algebra', 'url': '/algebra'},
    {'name': 'Contact', 'url': '/contact'}
    #{'name': 'Signup', 'url': '/signup'}
]

@home_bp.route('/')
def index():
    return render_template(
        'index.html',
        title='Math Worksheet Generator',
        subtitle='Sean & Eric collaborates'
    )

@home_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.html",
        form=form,
        template="form-template"
    )

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

# error handlers

@home_bp.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(
        render_template("404.html"),
        404
     )


@home_bp.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(
        render_template("400.html"),
        400
    )


@home_bp.errorhandler(500)
def server_error():
    """Internal server error."""
    return make_response(
        render_template("500.html"),
        500
    )
'''