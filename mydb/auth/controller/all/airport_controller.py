from http import HTTPStatus

from flask import abort

from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import airport_service

class AirportController(GeneralController):
    _service = airport_service

    def find_airlines_by_airport_id(self, airport_id):
        airlines = self._service.find_airlines_by_airport_id(airport_id)
        if airlines is None:
            abort(HTTPStatus.NOT_FOUND)
        return [airline.put_into_dto() for airline in airlines]

    def find_all_airlines_for_all_airports(self):
        airports_airlines = self._service.find_all_airlines_for_all_airports()
        print(airports_airlines)
        if airports_airlines is None:
            abort(HTTPStatus.NOT_FOUND)

        response_data = []
        for airport_icao, data in airports_airlines.items():
            airlines_data = data.get("airlines", [])

            response_data.append({
                "airport_icao": airport_icao,
                "airlines": [
                    airline.put_into_dto() if hasattr(airline, 'put_into_dto') else airline
                    for airline in airlines_data
                ] if airlines_data else []
            })
        # print(response_data)
        return response_data

    def find_flights_by_airport_id(self, airport_id):
        flights = self._service.find_flights_by_airport_id(airport_id)
        if flights is None:
            abort(HTTPStatus.NOT_FOUND)
        return [flight.put_into_dto() for flight in flights]

    def find_all_flights_for_all_airports(self):
        airports_flights = self._service.find_all_flights_for_all_airports()
        print(airports_flights)
        if airports_flights is None:
            abort(HTTPStatus.NOT_FOUND)

        response_data = []
        for airport_icao, data in airports_flights.items():
            flights_data = data.get("flights", [])

            response_data.append({
                "airport_icao": airport_icao,
                "flights": [
                    flight.put_into_dto() if hasattr(flight, 'put_into_dto') else flight
                    for flight in flights_data
                ] if flights_data else []
            })
        # print(response_data)
        return response_data