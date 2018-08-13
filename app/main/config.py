import os

# mysql_local_base = os.environ['DATABASE_URL']
mysql_local_base = 'mysql://bookuser:password1@localhost/book_db'

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
  DEBUG = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  RESTPLUS_MASK_SWAGGER = False
  SWAGGER_UI_DOC_EXPANSION = 'full'

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = mysql_local_base
  SQLALCHEMY_ECHO = True

class TestingConfig(Config):
  DEBUG = True
  TESTING = True
  PRESERVE_CONTEXT_ON_EXCEPTION = False 

class ProductionConfig(Config):
  DEBUG = False
  # SQLALCHEMY_DATABASE_URI = mysql_local_base

config_by_name = dict(
  dev=DevelopmentConfig,
  test=TestingConfig,
  prod=ProductionConfig
)

key = Config.SECRET_KEY
