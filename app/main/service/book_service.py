from . import db
from app.main.model.book import Book
from app.main.model.author import Author
from sqlalchemy import or_
from urllib.parse import unquote
from pdb import set_trace

def get_all_books():
  return Book.query.all()

def get_book(filter, value):
  if (filter == 'title'):
    bookQuery = Book.query.filter(Book.title.like('%'+value+'%'))
    return bookQuery.all()
  elif (filter == 'author'):
    likeFirstName = Author.first_name.like('%'+value+'%')
    likeLastName = Author.last_name.like('%'+value+'%')
    likeEmail = Author.email.like('%'+value+'%')
    authorQuery = Book.query \
              .join(Author) \
              .filter(or_(
                or_(likeFirstName, likeLastName), 
                likeEmail
              ))
    return authorQuery.all()
  else:
    return None

