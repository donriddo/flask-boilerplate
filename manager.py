# coding: utf-8
import os
from flask_script import Manager
from flask import redirect
from src import create_app
# Used by app debug & livereload
PORT = 7070
if os.environ.get('PORT'):
    PORT = os.environ.get('PORT')
app = create_app()
manager = Manager(app)


@app.route('/')
def apidocs():
    return redirect('/apidocs')


@manager.command
def run():
    """Run app."""
    app.run(host='0.0.0.0', port=PORT)


if __name__ == "__main__":
    manager.run()
