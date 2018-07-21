import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from pdb import set_trace

# When regular package imported, __init__.py file is implicitly executed, and the objects it defines are bound to names in the package’s namespace
# thus, these imports are within __init__.py
from app.main import create_app, db

app = create_app(os.getenv('APP_ENV') or 'dev')

# instantiate necessary classes
manager = Manager(app)
migrate = Migrate(app, db)

# expose database migration commands to the command line
manager.add_command('db', MigrateCommand)

# expose command to start the app to the command line
@manager.command
def run():
  host = os.environ.get('IP', '0.0.0.0')
  port = int(os.environ.get('PORT', 5000))
  app.run(host=host, port=port)

if __name__ == "__main__":
  # prepare manager instance to receive input from command line
  manager.run()

