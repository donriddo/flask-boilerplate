#!/usr/bin/env python
# encoding: utf-8
import json
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, request, jsonify, make_response
from src.users.user_repo import create_user, delete_user, fetch_all_users, fetch_user, update_user
from setup import cache

user_api = Blueprint('user', __name__)


@user_api.route('/', methods=['POST'])
def create_new_user():
    info = json.loads(request.data)
    user = None
    try:
        user = create_user(info)
    except IntegrityError:
        return make_response(
            jsonify({"status": 400, "message": "user already exists"}),
            400
        )

    if user:
        cache.clear()
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
@cache.cached(query_string=True)
def list_users():
    page = 1
    per_page = 10
    print(request.path)
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


@user_api.route('/<int:id>', methods=['GET'])
@cache.cached(query_string=True)
def get_user_info(id):
    user = fetch_user(id)
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


@user_api.route('/<int:id>', methods=['PUT'])
def update_user_info(id):
    user = update_user(id, json.loads(request.data))
    if user:
        cache.clear()
        return make_response(
            jsonify({
                "status": 200,
                "message": "user updated successfully",
                "data": user
            }),
            200
        )
    else:
        return make_response(
            jsonify({"status": 404, "message": "user not found"}),
            404
        )


@user_api.route('/<int:id>', methods=['DELETE'])
def delete_user_info(id):
    user = delete_user(id)
    if user:
        cache.clear()
        return make_response(
            jsonify({
                "status": 200,
                "message": "user deleted successfully",
                "data": user
            }),
            200
        )
    else:
        return make_response(
            jsonify({"status": 404, "message": "user not found"}),
            404
        )
