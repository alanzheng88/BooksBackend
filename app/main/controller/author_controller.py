from flask_restplus import Resource, Namespace, fields
from app.main.service.author_service import get_all_authors

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

@ns.route('/')
class AuthorList(Resource):
  @ns.doc(
    description = 'Get a list of authors',
    responses = {
      200: 'List of authors fetched successfully'
    }
  )
  @ns.marshal_list_with(author)
  def get(self):
    return get_all_authors()
