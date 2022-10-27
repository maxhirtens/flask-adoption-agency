'''Models for adoption app.'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
  '''Pet to adopt.'''

  __tablename__ = 'pets'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.Text, nullable=False)
  species = db.Column(db.Text, nullable=False)
  photo_url = db.Column(db.Text, default='https://www.pinclipart.com/picdir/middle/192-1925693_there-is-a-side-view-of-a-dog.png')
  age = db.Column(db.Integer)
  notes = db.Column(db.Text)
  available = db.Column(db.Boolean, default=True, nullable=False)

def connect_db(app):
    db.app = app
    db.init_app(app)
