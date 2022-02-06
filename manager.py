# coding: utf-8
import os
from flask_script import Manager
from src import create_app
# Used by app debug & livereload
PORT = 7070
if os.environ.get('PORT'):
    PORT = os.environ.get('PORT')
app = create_app()
manager = Manager(app)


@manager.command
def run():
    """Run app."""
    app.run(host='0.0.0.0', port=PORT)


if __name__ == "__main__":
    manager.run()
