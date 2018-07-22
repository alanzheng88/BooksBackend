from . import db

# model for storing book related details
class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(80), unique=True, nullable=False)
  author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
  
  def __repr__(self):
    return "<Book id={} title='{}'>".format(self.id, self.title)

