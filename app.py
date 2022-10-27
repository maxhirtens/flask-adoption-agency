'''Routes for adoption app.'''

from flask import Flask, url_for, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SECRET_KEY'] = "boomerang"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adoption_agency"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route('/')
def list_pets():
  '''Shows pet homepage.'''

  pets = Pet.query.all()
  return render_template('petlist.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
  '''Shows new pet form.'''

  form = AddPetForm()

  if form.validate_on_submit():
    return redirect('/')
  else:
    return render_template('addpet.html', form=form)
