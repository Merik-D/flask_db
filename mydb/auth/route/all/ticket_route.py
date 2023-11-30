from http import HTTPStatus
from flask import Blueprint, jsonify, Response, make_response, request
from mydb.auth.controller import ticket_controller
from mydb.auth.domain.all.ticket import Ticket

ticket_bp = Blueprint("tickets", __name__, url_prefix="/tickets/")


@ticket_bp.get("")
def get_all_tickets() -> Response:
    return make_response(jsonify(ticket_controller.find_all()), HTTPStatus.OK)

@ticket_bp.post("")
def create_ticket() -> Response:
    content = request.get_json()
    ticket = Ticket.create_from_dto(content)
    ticket_id = ticket_controller.create(ticket)
    return make_response(f"Ticket created with ID: {ticket_id}", HTTPStatus.CREATED)

@ticket_bp.get('/<int:ticket_id>')
def get_ticket(ticket_id: int) -> Response:
    return make_response(jsonify(ticket_controller.find_by_id(ticket_id)), HTTPStatus.OK)

@ticket_bp.put('/<int:ticket_id>')
def update_ticket(ticket_id: int) -> Response:
    content = request.get_json()
    ticket = Ticket.create_from_dto(content)
    ticket_controller.update(ticket_id, ticket)
    return make_response("Ticket updated", HTTPStatus.OK)

@ticket_bp.patch('/<int:ticket_id>')
def patch_ticket(ticket_id: int) -> Response:
    content = request.get_json()
    ticket_controller.patch(ticket_id, content)
    return make_response("Ticket patched", HTTPStatus.OK)

@ticket_bp.delete('/<int:ticket_id>')
def delete_ticket(ticket_id: int) -> Response:
    ticket_controller.delete(ticket_id)
    return make_response("Ticket deleted", HTTPStatus.OK)
