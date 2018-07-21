from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config_by_name
from ..__init__ import api
#from pdb import set_trace

db = SQLAlchemy()

# config_name is an object with the following keys: dev, test, prod
def create_app(config_name):
  app = Flask(__name__)
  # merge my custom configs into the default app.config
  app.config.from_object(config_by_name[config_name])
  api.init_app(app)
  db.init_app(app)  
  return app
