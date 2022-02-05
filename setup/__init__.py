from setup.postgres import postgres
from flask_migrate import Migrate

db = postgres


def setup_db(app):
    db.init_app(app)
    migrate = Migrate(app, db)
