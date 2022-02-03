# coding: utf-8
import os
class ProductionConfig(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    TESTING = False
    SECRET_KEY = "your_key"
    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # MongoEngine config
    MONGODB_SETTINGS = {
        'db': 'flask_db',
        'host': 'localhost',
        'port': 27017
    }
