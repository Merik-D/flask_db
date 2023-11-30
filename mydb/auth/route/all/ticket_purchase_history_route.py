from http import HTTPStatus
from flask import Blueprint, jsonify, Response, make_response, request
from mydb.auth.controller import ticket_purchase_history_controller
from mydb.auth.domain.all.ticket_purchase_history import TicketPurchaseHistory

ticket_purchase_history_bp = Blueprint("ticket_purchase_histories", __name__, url_prefix="/ticket_purchase_histories/")


@ticket_purchase_history_bp.get("")
def get_all_ticket_purchase_histories() -> Response:
    return make_response(jsonify(ticket_purchase_history_controller.find_all()), HTTPStatus.OK)

@ticket_purchase_history_bp.post("")
def create_ticket_purchase_history() -> Response:
    content = request.get_json()
    ticket_purchase_history = TicketPurchaseHistory.create_from_dto(content)
    ticket_purchase_history_id = ticket_purchase_history_controller.create(ticket_purchase_history)
    return make_response(f"Ticket purchase history created with ID: {ticket_purchase_history_id}", HTTPStatus.CREATED)

@ticket_purchase_history_bp.get('/<int:history_id>')
def get_ticket_purchase_history(history_id: int) -> Response:
    return make_response(jsonify(ticket_purchase_history_controller.find_by_id(history_id)), HTTPStatus.OK)

@ticket_purchase_history_bp.put('/<int:history_id>')
def update_ticket_purchase_history(history_id: int) -> Response:
    content = request.get_json()
    ticket_purchase_history = TicketPurchaseHistory.create_from_dto(content)
    ticket_purchase_history_controller.update(history_id, ticket_purchase_history)
    return make_response("Ticket purchase history updated", HTTPStatus.OK)

@ticket_purchase_history_bp.patch('/<int:history_id>')
def patch_ticket_purchase_history(history_id: int) -> Response:
    content = request.get_json()
    ticket_purchase_history_controller.patch(history_id, content)
    return make_response("Ticket purchase history patched", HTTPStatus.OK)

@ticket_purchase_history_bp.delete('/<int:history_id>')
def delete_ticket_purchase_history(history_id: int) -> Response:
    ticket_purchase_history_controller.delete(history_id)
    return make_response("Ticket purchase history deleted", HTTPStatus.OK)

@ticket_purchase_history_bp.get('/user/<int:user_id>/tickets')
def get_user_tickets(user_id: int) -> Response:
    user_tickets = ticket_purchase_history_controller.find_user_tickets(user_id)
    return make_response(jsonify(user_tickets), HTTPStatus.OK)

@ticket_purchase_history_bp.get('/ticket/<int:ticket_id>/user')
def get_user_by_ticket(ticket_id: int) -> Response:
    user_by_ticket = ticket_purchase_history_controller.find_user_by_ticket(ticket_id)
    return make_response(jsonify(user_by_ticket), HTTPStatus.OK)

@ticket_purchase_history_bp.get('/tickets/')
def get_all_tickets_for_all_users() -> Response:
    list_history = ticket_purchase_history_controller.find_all_tickets_for_all_users()
    return make_response(jsonify(list_history), HTTPStatus.OK)