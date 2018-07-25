from flask_restplus import Resource, Namespace, fields
from app.main.service.author_service import get_all_authors

ns = Namespace(
  name = 'authors',
  description = 'authors related operations'
)

author = ns.model('author', {
  'id': fields.Integer(required=True, description='Author Id'),
  'first_name': fields.String,
  'last_name': fields.String,
  'email': fields.String
})

@ns.route('/')
class AuthorList(Resource):
  @ns.marshal_list_with(author)
  def get(self):
    return get_all_authors()
