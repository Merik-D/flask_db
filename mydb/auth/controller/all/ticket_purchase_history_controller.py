from http import HTTPStatus

from flask import abort

from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.domain import Ticket, TicketPurchaseHistory, User
from mydb.auth.service import ticket_purchase_history_service


class TicketPurchaseHistoryController(GeneralController):
    _service = ticket_purchase_history_service

    def find_user_tickets(self, user_id: int):
        tickets = self._service.find_user_tickets(user_id)
        if tickets is None:
            abort(HTTPStatus.NOT_FOUND)
        return [ticket.put_into_dto() for ticket in tickets]

    def find_user_by_ticket(self, ticket_id: int):
        user = self._service.find_user_by_ticket(ticket_id)
        if user is None:
            abort(HTTPStatus.NOT_FOUND)
        return user.put_into_dto()

    def find_all_tickets_for_all_users(self):
        tickets_for_all_users = self._service.find_all_tickets_for_all_users()

        if tickets_for_all_users is None:
            abort(HTTPStatus.NOT_FOUND)

        response_data = []
        for user, data in tickets_for_all_users.items():
            if isinstance(data, list):
                user_tickets_data = data
            else:
                user_tickets_data = data.get("tickets", [])

            response_data.append({
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "surname": user.surname,
                },
                "tickets": [
                    ticket.put_into_dto() if hasattr(ticket, 'put_into_dto') else ticket
                    for ticket in user_tickets_data
                ] if user_tickets_data else []
            })

        return response_data
