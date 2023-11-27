from mydb.auth.dao import ticket_dao
from mydb.auth.service.general_service import GeneralService


class TicketService(GeneralService):
    _dao = ticket_dao