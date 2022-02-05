# coding: utf-8
import os


class TestConfig(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    TESTING = False
    # Root path of project
    PROJECT_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_DATABASE_URI')
    # MongoEngine config
    MONGODB_SETTINGS = {
        'db': 'flask_db',
        'host': 'localhost',
        'port': 27017
    }
