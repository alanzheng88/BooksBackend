from flask import Flask, Response, abort, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/books')
def book_list():
  books = [
    {
      'id': 1,
      'title': 'JavaScript - The Complete Guide',
      'author': {
        'firstName': 'Alexander',
        'lastName': 'Great'
      }
    },
    {
      'id': 2,
      'title': 'Java - The New Beginning',
      'author': {
        'firstName': 'Frances',
        'lastName': 'Ong'
      }
    }
  ]
  response = jsonify(books)
  response.status_code = 200
  return response

@app.errorhandler(404)
def page_not_found(error):
  return "The API is ready!"