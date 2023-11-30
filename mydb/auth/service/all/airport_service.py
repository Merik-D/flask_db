from mydb.auth.service.general_service import GeneralService
from mydb.auth.dao import airport_dao

class AirportService(GeneralService):
    _dao = airport_dao

    def find_airlines_by_airport_id(self, airport_id):
        return self._dao.find_airlines_by_airport_id(airport_id)

    def find_all_airlines_for_all_airports(self):
        return self._dao.find_all_airlines_for_all_airports()

    def find_flights_by_airport_id(self, airport_id):
        return self._dao.find_flights_by_airport_id(airport_id)

    def find_all_flights_for_all_airports(self):
        return self._dao.find_all_flights_for_all_airports()
