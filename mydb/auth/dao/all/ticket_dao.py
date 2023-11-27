from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.all.ticket import Ticket


class TicketDao(GeneralDAO):
    _domain_type = Ticket