from mydb.auth.dao import ticket_purchase_history_dao
from mydb.auth.service.general_service import GeneralService


class TicketPurchaseHistoryService(GeneralService):
    _dao = ticket_purchase_history_dao

    def find_user_tickets(self, user_id: int):
        return self._dao.find_user_tickets(user_id)

    def find_user_by_ticket(self, ticket_id: int):
        return self._dao.find_user_by_ticket(ticket_id)

    def find_all_tickets_for_all_users(self):
        return self._dao.find_all_tickets_for_all_users()