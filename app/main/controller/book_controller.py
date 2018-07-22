from flask_restplus import Resource, Namespace, fields, reqparse
from app.main.service.book_service import get_all_books
#from pdb import set_trace

ns = Namespace('books', description='books related operations')

book = ns.model('book', {
  'id': fields.Integer(required=True, description='Id'),
  'title': fields.String(required=True, description='Book Title')
})

@ns.route('/')
class BookList(Resource):
  @ns.marshal_with(book)
  def get(self):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, location='args')
    args = parser.parse_args()
    if (args.title is not None):
      print('title in query string is: ', args.title)
    return get_all_books()

