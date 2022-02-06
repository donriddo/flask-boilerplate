from flask_migrate import Migrate
from setup.postgres import postgres
from setup.redis import redis_client
from setup.cache import cache_interface
from setup.documentation import swagger_api

db = postgres
redis = redis_client
cache = cache_interface
swagger = swagger_api


def setup_db(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def setup_redis(app):
    redis.init_app(app)


def setup_cache(app):
    cache.init_app(app)


def setup_documentation(app):
    swagger.init_app(app)
