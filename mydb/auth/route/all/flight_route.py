from http import HTTPStatus
from flask import Blueprint, jsonify, Response, make_response, request
from mydb.auth.controller import flight_controller
from mydb.auth.domain.all.flight import Flight

flight_bp = Blueprint("flights", __name__, url_prefix="/flights/")


@flight_bp.get("")
def get_all_flights() -> Response:
    return make_response(jsonify(flight_controller.find_all()), HTTPStatus.OK)

@flight_bp.post("")
def create_flight() -> Response:
    content = request.get_json()
    flight = Flight.create_from_dto(content)
    flight_id = flight_controller.create(flight)
    return make_response(f"Flight created with ID: {flight_id}", HTTPStatus.CREATED)

@flight_bp.get('/<int:flight_id>')
def get_flight(flight_id: int) -> Response:
    return make_response(jsonify(flight_controller.find_by_id(flight_id)), HTTPStatus.OK)

@flight_bp.put('/<int:flight_id>')
def update_flight(flight_id: int) -> Response:
    content = request.get_json()
    flight = Flight.create_from_dto(content)
    flight_controller.update(flight_id, flight)
    return make_response("Flight updated", HTTPStatus.OK)

@flight_bp.patch('/<int:flight_id>')
def patch_flight(flight_id: int) -> Response:
    content = request.get_json()
    flight_controller.patch(flight_id, content)
    return make_response("Flight patched", HTTPStatus.OK)

@flight_bp.delete('/<int:flight_id>')
def delete_flight(flight_id: int) -> Response:
    flight_controller.delete(flight_id)
    return make_response("Flight deleted", HTTPStatus.OK)
