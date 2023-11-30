from mydb.auth.dao import flight_dao
from mydb.auth.service.general_service import GeneralService


class FlightService(GeneralService):
    _dao = flight_dao