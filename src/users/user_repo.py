from setup import db
from src.users.user_model import User

def create_user(record):
  user = User(name=record['name'],email=record['email'])
  user.save()
  return user.to_json()

def fetch_user(name=None, email=None):
  user = User.objects(name=name,email=email).first()
  if user:
    return user.to_json()
  else:
    return None

def fetch_all_users():
  users = User.objects().all()
  return users
