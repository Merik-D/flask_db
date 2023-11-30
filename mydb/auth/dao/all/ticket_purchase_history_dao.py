from sqlalchemy.orm import aliased

from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain import Ticket, User
from mydb.auth.domain.all.ticket_purchase_history import TicketPurchaseHistory


class TicketPurchaseHistoryDao(GeneralDAO):
    _domain_type = TicketPurchaseHistory

    def find_user_tickets(self, user_id: int):
        user_tickets = (
            self._session.query(Ticket)
            .join(TicketPurchaseHistory)
            .filter(TicketPurchaseHistory.user_id == user_id)
            .all()
        )
        return user_tickets

    def find_user_by_ticket(self, ticket_id: int):
        user_by_ticket = (
            self._session.query(User)
            .join(TicketPurchaseHistory)
            .filter(TicketPurchaseHistory.ticket_id == ticket_id)
            .first()
        )
        return user_by_ticket

    def find_all_tickets_for_all_users(self):
        ticket_alias = aliased(Ticket)
        history_alias = aliased(TicketPurchaseHistory)

        users_and_tickets = (
            self._session.query(User, ticket_alias)
            .join(history_alias, User.id == history_alias.user_id)
            .join(ticket_alias, history_alias.ticket_id == ticket_alias.id)
            .all()
        )

        user_tickets_dict = {}
        for user, ticket in users_and_tickets:
            if user not in user_tickets_dict:
                user_tickets_dict[user] = []
            user_tickets_dict[user].append(ticket.put_into_dto())

        return user_tickets_dict