'''WTForms for adoption app.'''

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
  '''Easy form to add pets.'''
  name = StringField('Pet Name'),
  species = StringField('Species'),
  photo_url = StringField('Photo URL'),
  age = IntegerField('Age'),
  notes = TextAreaField('Notes')
