from flask_restplus import Api
from .main.controller.book_controller import ns as book_ns
from .main.controller.author_controller import ns as author_ns

api = Api(
  version='1.0',
  title='Books Webservice',
  description='Manage a library of books',
  contact='alanzhengg@gmail.com'
)

api.add_namespace(book_ns, path='/books')
api.add_namespace(author_ns, path='/authors')
