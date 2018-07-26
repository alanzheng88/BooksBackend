from flask_restplus import Resource, Namespace, fields, reqparse
from app.main.service.book_service import get_all_books, get_book
from app.main.util.book_dto import BookDto
from werkzeug.exceptions import BadRequest
#from pdb import set_trace

ns = BookDto.ns
_book = BookDto.book

@ns.route('/')
class BookList(Resource):
  @ns.doc(
    description = 'Get a list of books',
    params = {
      'title': 'filter parameter'
    },
    responses = {
      200: 'List of books fetched successfully'
    }
  )
  @ns.marshal_list_with(_book)
  def get(self):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, location='args')
    params = parser.parse_args()
    data = None
    if (params.title is None):
      print('getting all books')
      data = get_all_books()
    else:
      print('title in query string is: ', params.title)
      data = get_book('title', params.title)

    return data

