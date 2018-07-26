from flask_restplus import Namespace, fields

class BookDto:
  ns = Namespace(
    name = 'books', 
    description = 'books related operations'
  )
  book = ns.model('book', {
    'id': fields.Integer(required=True, description='Book Id'),
    'title': fields.String(required=True, description='Book Title'),
    'author': {
      'first_name': fields.String(attribute=lambda x: x.the_author.first_name),
      'last_name': fields.String(attribute=lambda x: x.the_author.last_name),
      'email': fields.String(attribute=lambda x: x.the_author.email)
    }
  })