from http import HTTPStatus

from flask import Blueprint, jsonify, Response, make_response, request
from mydb.auth.controller import user_controller
from mydb.auth.domain import User

user_bp = Blueprint("users", __name__, url_prefix="/users/")


@user_bp.get("")
def get_all_users() -> Response:
    return make_response(jsonify(user_controller.find_all()), HTTPStatus.OK)

@user_bp.post("")
def create_user() -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_id = user_controller.create(user)
    return make_response(f"User created with ID: {user_id}", HTTPStatus.CREATED)

@user_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    return make_response(jsonify(user_controller.find_by_id(user_id)), HTTPStatus.OK)

@user_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.update(user_id, user)
    return make_response("User updated", HTTPStatus.OK)

@user_bp.patch('/<int:user_id>')
def patch_user(user_id: int) -> Response:
    content = request.get_json()
    user_controller.patch(user_id, content)
    return make_response("User patched", HTTPStatus.OK)

@user_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    user_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)