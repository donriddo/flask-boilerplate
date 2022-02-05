#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Blueprint, request, jsonify, make_response
from src.users.user_repo import create_user, fetch_all_users, fetch_user

user_api = Blueprint('user', __name__)


@user_api.route('/', methods=['POST'])
def create_new_user():
    info = json.loads(request.data)
    email = info.get('email', '')
    first_name = info.get('first_name', '')
    last_name = info.get('last_name', '')
    user = create_user(
        {"email": email, "first_name": first_name, "last_name": last_name})
    if user:
        return make_response(
            jsonify({
                "status": 200,
                "message": "created successfully",
                "data": user
            }),
            200
        )
    else:
        return make_response(
            jsonify({"status": 400, "message": "error creating user"}),
            400
        )


@user_api.route('/', methods=['GET'])
def list_users():
    page = 1
    per_page = 10
    try:
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
    except:
        pass

    result = fetch_all_users(page=page, per_page=per_page)

    return make_response(
        {
            "status": 200,
            "message": "users retrieved successfully",
            "data": result["data"],
            "meta": result["meta"]
        },
        200
    )


@user_api.route('/:id', methods=['GET'])
def get_user_info():
    uid = request.params.get('id')
    first_name = request.args.get('first_name')
    email = request.args.get('email')
    user = fetch_user({"email": email, "first_name": first_name})
    if user:
        return make_response(
            jsonify({
                "status": 200,
                "message": "user retrieved successfully",
                "data": user
            }),
            200
        )
    else:
        return make_response(
            jsonify({"status": 404, "message": "user not found"}),
            404
        )
