from mydb.auth.dao import ticket_dao
from mydb.auth.service.general_service import GeneralService


class TicketService(GeneralService):
    _dao = ticket_dao

    def get_ticket_price_statistics(self, aggregate_type:str):
        return self._dao.get_ticket_price_statistics(aggregate_type)