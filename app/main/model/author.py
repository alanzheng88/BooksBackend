from . import db
from pdb import set_trace

# model for storing author related details
class Author(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80), nullable=False)
  last_name = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(254), unique=True, nullable=False)
  books = db.relationship('Book', backref='the_author', lazy='joined')

  def __repr__(self):
    return "<Author id={} first_name='{}' last_name='{}' email='{}'>"\
                    .format(self.id,
                            self.first_name,
                            self.last_name,
                            self.email)
