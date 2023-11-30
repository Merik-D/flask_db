from http import HTTPStatus
from flask import Blueprint, jsonify, Response, make_response, request
from mydb.auth.controller import airport_controller
from mydb.auth.domain.all.airport import Airport

airport_bp = Blueprint("airports", __name__, url_prefix="/airports/")


@airport_bp.get("")
def get_all_airports() -> Response:
    return make_response(jsonify(airport_controller.find_all()), HTTPStatus.OK)

@airport_bp.post("")
def create_airport() -> Response:
    content = request.get_json()
    airport = Airport.create_from_dto(content)
    airport_id = airport_controller.create(airport)
    return make_response(f"Airport created with ID: {airport_id}", HTTPStatus.CREATED)

@airport_bp.get('/<int:airport_id>')
def get_airport(airport_id: int) -> Response:
    return make_response(jsonify(airport_controller.find_by_id(airport_id)), HTTPStatus.OK)

@airport_bp.put('/<int:airport_id>')
def update_airport(airport_id: int) -> Response:
    content = request.get_json()
    airport = Airport.create_from_dto(content)
    airport_controller.update(airport_id, airport)
    return make_response("Airport updated", HTTPStatus.OK)

@airport_bp.patch('/<int:airport_id>')
def patch_airport(airport_id: int) -> Response:
    content = request.get_json()
    airport_controller.patch(airport_id, content)
    return make_response("Airport patched", HTTPStatus.OK)

@airport_bp.delete('/<int:airport_id>')
def delete_airport(airport_id: int) -> Response:
    airport_controller.delete(airport_id)
    return make_response("Airport deleted", HTTPStatus.OK)

@airport_bp.get('/<int:airport_id>/airlines')
def get_airline_airports(airport_id: int)-> Response:
    return make_response(jsonify(airport_controller.find_airlines_by_airport_id(airport_id)), HTTPStatus.OK)

@airport_bp.get('/airlines')
def get_all_airlines_with_airports() -> Response:
    return make_response(jsonify(airport_controller.find_all_airlines_for_all_airports()), HTTPStatus.OK)

@airport_bp.get('/<int:airport_id>/flights')
def get_airport_flights(airport_id: int) -> Response:
    return make_response(jsonify(airport_controller.find_flights_by_airport_id(airport_id)), HTTPStatus.OK)

@airport_bp.get('/flights')
def get_all_flights_for_all_airports() -> Response:
    return make_response(jsonify(airport_controller.find_all_flights_for_all_airports()), HTTPStatus.OK)
