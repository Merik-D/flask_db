from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import ticket_service


class TicketController(GeneralController):
    _service = ticket_service

    def get_ticket_price_statistics(self, aggregate_type:str):
        return self._service.get_ticket_price_statistics(aggregate_type)[0][0]