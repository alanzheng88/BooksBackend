from flask_restplus import Namespace, fields

class AuthorDto:
  ns = Namespace(
    name = 'authors',
    description = 'authors related operations'
  )

  author = ns.model('author', {
    'id': fields.Integer(required=True, description='Author Id'),
    'first_name': fields.String(required=True, description='Author first name'),
    'last_name': fields.String(required=True, description='Author last name'),
    'email': fields.String(required=True, description='Author email')
  })