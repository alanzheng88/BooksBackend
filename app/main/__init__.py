from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import config_by_name
#from pdb import set_trace

db = SQLAlchemy()
# ORDER MATTERS!!!! DB MUST INIT BEFORE API
# since api need to refer to db instance
# at certain points
# SEE: https://stackoverflow.com/questions/41828711/flask-blueprint-sqlalchemy-cannot-import-name-db-into-moles-file
from app.__init__ import api

# config_name is an object with the following keys: dev, test, prod
def create_app(config_name):
  app = Flask(__name__)
  CORS(app)
  # merge my custom configs into the default app.config
  app.config.from_object(config_by_name[config_name])
  api.init_app(app)
  db.init_app(app)
  return app