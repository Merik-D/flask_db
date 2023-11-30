from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import flight_service


class FlightController(GeneralController):
    _service = flight_service