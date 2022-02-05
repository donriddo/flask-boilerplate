# coding: utf-8
import os


class DevelopmentConfig(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    TESTING = False
    SECRET_KEY = "your_key"
    # Root path of project
    PROJECT_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))
    # os.environ.get('POSTGRES_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/flask-app'

    # MongoEngine config
    MONGODB_SETTINGS = {
        'db': 'flask_db',
        'host': 'localhost',
        'port': 27017
    }
