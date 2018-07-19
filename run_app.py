import os

from api.book.app import app

if __name__ == '__main__':
  app.debug = True
  host = os.environ.get('IP', '0.0.0.0')
  port = int(os.environ.get('PORT', 5000))
  app.run(host=host, port=port)
