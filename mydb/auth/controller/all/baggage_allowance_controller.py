from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import baggage_allowance_service


class BaggageAllowanceController(GeneralController):
    _service = baggage_allowance_service