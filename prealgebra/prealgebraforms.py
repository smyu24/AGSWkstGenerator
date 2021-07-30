from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField  
#from wtforms.validators import DataRequired

class DecimalPlace(FlaskForm):
    min = IntegerField('Minimum')
    max = IntegerField('Maximum')
    diff = RadioField('Difficulty', choices = [('Easy'),('Medium'),('Hard')])