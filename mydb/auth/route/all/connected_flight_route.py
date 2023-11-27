from http import HTTPStatus
from flask import Blueprint, jsonify, Response, make_response, request
from mydb.auth.controller import connected_flight_controller
from mydb.auth.domain.all.connected_flight import ConnectedFlight

connected_flight_bp = Blueprint("connected_flights", __name__, url_prefix="/connected_flights/")


@connected_flight_bp.get("")
def get_all_connected_flights() -> Response:
    return make_response(jsonify(connected_flight_controller.find_all()), HTTPStatus.OK)

@connected_flight_bp.post("")
def create_connected_flight() -> Response:
    content = request.get_json()
    connected_flight = ConnectedFlight.create_from_dto(content)
    connected_flight_id = connected_flight_controller.create(connected_flight)
    return make_response(f"Connected Flight created with ID: {connected_flight_id}", HTTPStatus.CREATED)

@connected_flight_bp.get('/<int:connected_flight_id>')
def get_connected_flight(connected_flight_id: int) -> Response:
    return make_response(jsonify(connected_flight_controller.find_by_id(connected_flight_id)), HTTPStatus.OK)

@connected_flight_bp.put('/<int:connected_flight_id>')
def update_connected_flight(connected_flight_id: int) -> Response:
    content = request.get_json()
    connected_flight = ConnectedFlight.create_from_dto(content)
    connected_flight_controller.update(connected_flight_id, connected_flight)
    return make_response("Connected Flight updated", HTTPStatus.OK)

@connected_flight_bp.patch('/<int:connected_flight_id>')
def patch_connected_flight(connected_flight_id: int) -> Response:
    content = request.get_json()
    connected_flight_controller.patch(connected_flight_id, content)
    return make_response("Connected Flight patched", HTTPStatus.OK)

@connected_flight_bp.delete('/<int:connected_flight_id>')
def delete_connected_flight(connected_flight_id: int) -> Response:
    connected_flight_controller.delete(connected_flight_id)
    return make_response("Connected Flight deleted", HTTPStatus.OK)
