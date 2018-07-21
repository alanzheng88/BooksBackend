from flask import request
from flask_restplus import Resource, Namespace, fields

ns = Namespace('books', description='books related operations')

book = ns.model('Book', {
  'id': fields.Integer(required=True, description='Id'),
  'title': fields.String(required=True, description='Book Title')
})

@ns.route('/')
class BookList(Resource):
  @ns.marshal_with(book)
  def get(self): 
    books = [
      {
        'id': 1,
        'title': 'JavaScript - The Complete Guide'
      },
      {
        'id': 2,
        'title': 'Java - The New Beginning'
      }
    ]
    if (len(request.args) != 0):
      title = request.args.get("title")
      print('title in query string is: ', title)
    return books

