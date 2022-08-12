# forms.py
"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField, SelectField, IntegerField
#from wtfrecaptcha.fields import RecaptchaField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField( 'Name', [DataRequired()] )
    #email = EmailField('Email', [Email(message=('Not a valid email address.')), DataRequired()] )
    body = TextField( 'Message', [DataRequired(), Length(min=4, message=('Your message is too short.')) ] )
    #recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

class SignupForm(FlaskForm):
    """Sign up for a user account."""
    #email = StringField( 'Email', [ Email(message='Not a valid email address.'), DataRequired() ] )
    password = PasswordField( 'Password', [ DataRequired(message="Please enter a password."), ] )
    #confirmPassword = PasswordField( 'Repeat Password', [ EqualTo(password, message='Passwords must match.')] )
    title = SelectField( 'Title', [DataRequired()], choices=[ ('Student', 'Student'), ('Parents', 'Parents'), ] )
    bsdid = IntegerField( 'BSD id')
    #recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

