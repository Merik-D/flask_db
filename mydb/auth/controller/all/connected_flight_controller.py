from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import connected_flight_service


class ConnectedFlightController(GeneralController):
    _service = connected_flight_service