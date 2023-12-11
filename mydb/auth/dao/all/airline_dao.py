from sqlalchemy import text

from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.all.airline import Airline


class AirlineDao(GeneralDAO):
    _domain_type = Airline

    def find_airports_by_airline_id(self, airline_id):
        airline = self.find_by_id(airline_id)
        if airline:
            return airline.airports
        return None

    def find_all_airports_for_all_airlines(self):
        airlines = self.find_all()
        if airlines:
            airlines_data = {}
            for airline in airlines:
                airline_name = airline.name
                airports_for_airline = airline.airports
                airports_data = [airport.put_into_dto() for airport in airports_for_airline]

                if airline_name not in airlines_data:
                    airlines_data[airline_name] = {"airports": []}

                airlines_data[airline_name]["airports"].extend(airports_data)

            return airlines_data
        return None

    def link_airline_to_airport(self, airline_name, airport_ICAO):
        sql_statement = text("CALL insert_airline_airport(:airline_name, :airport_ICAO)")
        self._session.execute(sql_statement, {'airline_name': airline_name, 'airport_ICAO': airport_ICAO})
        self._session.commit()

