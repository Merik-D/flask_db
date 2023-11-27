from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.all.airport import Airport

class AirportDao(GeneralDAO):
    _domain_type = Airport

    def find_airlines_by_airport_id(self, airport_id):
        airport = self.find_by_id(airport_id)
        if airport:
            return airport.airlines
        return None

    def find_all_airlines_for_all_airports(self):
        airports = self.find_all()
        if airports:
            airports_data = {}
            for airport in airports:
                airport_icao = airport.ICAO
                airlines_for_airport = airport.airlines
                airlines_data = [airline.put_into_dto() for airline in airlines_for_airport]

                if airport_icao not in airports_data:
                    airports_data[airport_icao] = {"airlines": []}

                airports_data[airport_icao]["airlines"].extend(airlines_data)
            print(airports_data)
            return airports_data
        return None

    def find_flights_by_airport_id(self, airport_id):
        airport = self.find_by_id(airport_id)
        if airport:
            return airport.flights
        return None

    def find_all_flights_for_all_airports(self):
        airports = self.find_all()
        if airports:
            flights_data = {}
            for airport in airports:
                airport_icao = airport.ICAO
                flights_for_airport = airport.flights

                if airport_icao not in flights_data:
                    flights_data[airport_icao] = {"flights": []}

                flights_data[airport_icao]["flights"].extend([flight.put_into_dto() for flight in flights_for_airport])

            return flights_data
        return None
