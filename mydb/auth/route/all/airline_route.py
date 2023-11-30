from http import HTTPStatus

from flask import Blueprint, jsonify, Response, make_response, request
from mydb.auth.controller import airline_controller
from mydb.auth.domain.all.airline import Airline

airline_bp = Blueprint("airlines", __name__, url_prefix="/airlines/")


@airline_bp.get("")
def get_all_airlines() -> Response:
    return make_response(jsonify(airline_controller.find_all()), HTTPStatus.OK)

@airline_bp.post("")
def create_airline() -> Response:
    content = request.get_json()
    airline = Airline.create_from_dto(content)
    airline_id = airline_controller.create(airline)
    return make_response(f"User created with ID: {airline_id}", HTTPStatus.CREATED)

@airline_bp.get('/<int:airline_id>')
def get_airline(airline_id: int) -> Response:
    return make_response(jsonify(airline_controller.find_by_id(airline_id)), HTTPStatus.OK)

@airline_bp.put('/<int:airline_id>')
def update_airline(airline_id: int) -> Response:
    content = request.get_json()
    airline = Airline.create_from_dto(content)
    airline_controller.update(airline_id, airline)
    return make_response("Airline updated", HTTPStatus.OK)

@airline_bp.patch('/<int:airline_id>')
def patch_airline(airline_id: int) -> Response:
    content = request.get_json()
    airline_controller.patch(airline_id, content)
    return make_response("Airline patched", HTTPStatus.OK)

@airline_bp.delete('/<int:airline_id>')
def delete_airline(airline_id: int) -> Response:
    airline_controller.delete(airline_id)
    return make_response("Airline deleted", HTTPStatus.OK)

@airline_bp.get('/<int:airline_id>/airports')
def get_airline_airports(airline_id: int)-> Response:
    return make_response(jsonify(airline_controller.find_airports_by_airline_id(airline_id)), HTTPStatus.OK)

@airline_bp.get('/airports')
def get_all_airlines_with_airports() -> Response:
    return make_response(jsonify(airline_controller.find_all_airports_for_all_airlines()), HTTPStatus.OK)
