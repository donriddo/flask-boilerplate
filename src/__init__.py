# coding: utf-8
import sys
import os
# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)
import logging
from flask import Flask
# from flask_wtf import CsrfProtect
from config import load_config
from setup import setup_db
from src.users.user_controller import user_api

# convert python's encoding to utf8
try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except (AttributeError, NameError):
    pass

def create_app():
    """Create Flask app."""
    config = load_config()
    print(config)
    app = Flask(__name__)
    app.config.from_object(config)
    if not hasattr(app, 'production'):
        app.production = not app.debug and not app.testing
    # CSRF protect
    # CsrfProtect(app)
    if app.debug or app.testing:
        # Log errors to stderr in production mode
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.ERROR)
    # Register components
    setup_application(app)
    register_blueprints(app)
    return app

def setup_application(app):
    """Register models."""
    setup_db(app)

def register_blueprints(app):
    app.register_blueprint(user_api, url_prefix='/api/v1/users')
