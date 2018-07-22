from flask_restplus import Resource, Namespace, fields, reqparse
from app.main.service.book_service import get_all_books, get_book
# from pdb import set_trace

ns = Namespace('books', description='books related operations')

author = ns.model('author', {
  'id': fields.Integer(required=True, description='Author Id'),
  'first_name': fields.String,
  'last_name': fields.String,
  'email': fields.String
})

book = ns.model('book', {
  'id': fields.Integer(required=True, description='Book Id'),
  'title': fields.String(required=True, description='Book Title')
})

@ns.route('/')
class BookList(Resource):
  @ns.marshal_with(book)
  def get(self):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, location='args')
    args = parser.parse_args()
    data = None
    if (args.title is not None):
      print('title in query string is: ', args.title)
      data = get_book('title', args.title)
    else:
      data = get_all_books()
    return data

