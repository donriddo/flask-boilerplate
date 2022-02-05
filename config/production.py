# coding: utf-8
import os


class ProductionConfig(object):
    """Base config class."""
    # Flask app config
    DEBUG = True
    TESTING = False
    SECRET_KEY = "your_key"
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
    # Cache config
    CACHE_TYPE = 'RedisCache'
    CACHE_DEFAULT_TIMEOUT = os.environ.get('CACHE_TIMEOUT')
    REDIS_URL = os.environ.get('REDIS_URL')
    CACHE_REDIS_URL = REDIS_URL
