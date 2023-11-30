from http import HTTPStatus
from flask import Blueprint, jsonify, Response, make_response, request
from mydb.auth.controller import baggage_allowance_controller
from mydb.auth.domain.all.baggage_allowance import BaggageAllowance

baggage_bp = Blueprint("baggage_allowances", __name__, url_prefix="/baggage_allowances/")


@baggage_bp.get("")
def get_all_baggage_allowances() -> Response:
    return make_response(jsonify(baggage_allowance_controller.find_all()), HTTPStatus.OK)

@baggage_bp.post("")
def create_baggage_allowance() -> Response:
    content = request.get_json()
    baggage_allowance = BaggageAllowance.create_from_dto(content)
    baggage_allowance_id = baggage_allowance_controller.create(baggage_allowance)
    return make_response(f"Baggage Allowance created with ID: {baggage_allowance_id}", HTTPStatus.CREATED)

@baggage_bp.get('/<int:baggage_allowance_id>')
def get_baggage_allowance(baggage_allowance_id: int) -> Response:
    return make_response(jsonify(baggage_allowance_controller.find_by_id(baggage_allowance_id)), HTTPStatus.OK)

@baggage_bp.put('/<int:baggage_allowance_id>')
def update_baggage_allowance(baggage_allowance_id: int) -> Response:
    content = request.get_json()
    baggage_allowance = BaggageAllowance.create_from_dto(content)
    baggage_allowance_controller.update(baggage_allowance_id, baggage_allowance)
    return make_response("Baggage Allowance updated", HTTPStatus.OK)

@baggage_bp.patch('/<int:baggage_allowance_id>')
def patch_baggage_allowance(baggage_allowance_id: int) -> Response:
    content = request.get_json()
    baggage_allowance_controller.patch(baggage_allowance_id, content)
    return make_response("Baggage Allowance patched", HTTPStatus.OK)

@baggage_bp.delete('/<int:baggage_allowance_id>')
def delete_baggage_allowance(baggage_allowance_id: int) -> Response:
    baggage_allowance_controller.delete(baggage_allowance_id)
    return make_response("Baggage Allowance deleted", HTTPStatus.OK)
