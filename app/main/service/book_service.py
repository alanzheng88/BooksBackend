from . import db
from app.main.model.book import Book
from pdb import set_trace

def get_all_books():
  return Book.query.all()

def get_book(filter, value):
  if (filter == 'title'):
    return Book.query.filter(Book.title.like('%'+value+'%')).all()
  else:
    return None

