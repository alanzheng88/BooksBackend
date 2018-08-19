from . import db
from app.main.model.book import Book
from app.main.model.author import Author
from sqlalchemy import or_
from sqlalchemy.orm import joinedload
from urllib.parse import unquote
from pdb import set_trace

def __book_query():
  return Book.query \
              .join(Book.the_author) \
              .options(joinedload(Book.the_author))

def get_all_books(limit, afterId):
  return __book_query() \
          .order_by(Book.id) \
          .filter(Book.id > afterId) \
          .limit(limit) \
          .all()

def get_book(filter, value, limit, afterId):
  if (filter == 'title'):
    bookQuery = __book_query() \
                  .filter(Book.title.like('%'+value+'%')) \
                  .order_by(Book.id) \
                  .filter(Book.id > afterId) \
                  .limit(limit)
    return bookQuery.all()
  elif (filter == 'author'):
    likeFirstName = Author.first_name.like('%'+value+'%')
    likeLastName = Author.last_name.like('%'+value+'%')
    likeEmail = Author.email.like('%'+value+'%')
    authorQuery = __book_query() \
                      .filter(or_(
                        or_(likeFirstName, likeLastName), 
                        likeEmail
                      )) \
                      .order_by(Book.id) \
                      .filter(Book.id > afterId) \
                      .limit(limit)
    return authorQuery.all()
  else:
    return None

