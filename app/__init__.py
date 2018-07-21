from flask_restplus import Api
from .main.controller.book_controller import ns as book_ns

api = Api()

api.add_namespace(book_ns, path='/books')
