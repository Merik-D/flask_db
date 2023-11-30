from mydb.auth.dao import connected_flight_dao
from mydb.auth.service.general_service import GeneralService


class ConnectedFlightService(GeneralService):
    _dao = connected_flight_dao