from . import db
from app.main.model.author import Author
#from pdb import set_trace

def get_all_authors():
  return Author.query.all()