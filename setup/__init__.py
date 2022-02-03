from setup.mongo import mongo

db = mongo

def setup_db(app):
  db.init_app(app)
