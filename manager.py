# coding: utf-8
from flask_script import Manager
from src import create_app
# Used by app debug & livereload
PORT = 7070
app = create_app()
manager = Manager(app)

@manager.command
def run():
    """Run app."""
    app.run(port=PORT)

if __name__ == "__main__":
    manager.run()
