from flask_restplus import Resource, Namespace, fields
from app.main.service.author_service import get_all_authors
from app.main.util.author_dto import AuthorDto

ns = AuthorDto.ns
_author = AuthorDto.author

@ns.route('/')
class AuthorList(Resource):
  @ns.doc(
    description = 'Get a list of authors',
    responses = {
      200: 'List of authors fetched successfully'
    }
  )
  @ns.marshal_list_with(_author)
  def get(self):
    return get_all_authors()