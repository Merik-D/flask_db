from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import ticket_service


class TicketController(GeneralController):
    _service = ticket_service