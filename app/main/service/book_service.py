from . import db
from app.main.model.book import Book
#from pdb import set_trace

def get_all_books():
  return Book.query.all()

