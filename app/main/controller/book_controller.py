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
    return books

