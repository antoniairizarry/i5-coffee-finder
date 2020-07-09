from . import db 

class Movie(db.Model):
  #table columns
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50))
  rating = db.Column(db.Integer)