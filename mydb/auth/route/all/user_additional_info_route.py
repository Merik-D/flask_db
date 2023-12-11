from http import HTTPStatus

from flask import Blueprint, jsonify, Response, make_response

from mydb.auth.controller import user_additional_info_controller

user_additional_info_bp = Blueprint("user_additional_info", __name__, url_prefix="/user_additional_info/")

@user_additional_info_bp.post("")
def insert_packet_of_user_additional_info() -> Response:
    return make_response(jsonify(user_additional_info_controller.insert_packet_of_user_additional_info(), HTTPStatus.OK))