#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Blueprint, request, jsonify, make_response
from src.users.user_repo import create_user, fetch_all_users

user_api = Blueprint('user', __name__)

@user_api.route('/', methods=['POST'])
def create_new_user():
  info = json.loads(request.data)
  email = info.get('email', '')
  name = info.get('name', '')
  user = create_user({"email":email,"name":name})
  if user:
      return make_response(jsonify({"data":user}), 200)
  else:
      return make_response(
        jsonify({"status": 400, "message": "error creating user"}),
        400
      )

@user_api.route('/', methods=['GET'])
def list_users():
  users = fetch_all_users()
  return make_response(
        jsonify({
          "status": 200,
          "message": "users retrieved successfully",
          "data": users
        }),
        200
      )


@user_api.route('/:id', methods=['GET'])
def get_user_info():
  uid = request.params.get('id')
  name = request.args.get('name')
  email = request.args.get('email')
  user = fetch_user({"email":email,"name":name})
  if user:
      return make_response(jsonify({"data":user}), 200)
  else:
      return make_response(
        jsonify({"status": 404, "message": "user not found"}),
        404
      )

