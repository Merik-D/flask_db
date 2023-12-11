from mydb.auth.dao import airline_dao
from mydb.auth.service.general_service import GeneralService


class AirlineService(GeneralService):
    _dao = airline_dao

    def find_airports_by_airline_id(self, airline_id):
        return self._dao.find_airports_by_airline_id(airline_id)

    def find_all_airports_for_all_airlines(self):
        return self._dao.find_all_airports_for_all_airlines()

    def link_airline_to_airport(self, airline_name, airport_ICAO):
        return self._dao.link_airline_to_airport(airline_name, airport_ICAO)