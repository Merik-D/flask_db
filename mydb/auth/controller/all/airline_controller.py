from http import HTTPStatus
from flask import abort

from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import airline_service


class AirlineController(GeneralController):
    _service = airline_service

    def find_airports_by_airline_id(self, airline_id):
        airports = self._service.find_airports_by_airline_id(airline_id)
        if airports is None:
            abort(HTTPStatus.NOT_FOUND)
        return [airport.put_into_dto() for airport in airports]

    def find_all_airports_for_all_airlines(self):
        airlines_airports = self._service.find_all_airports_for_all_airlines()
        print(airlines_airports)
        if airlines_airports is None:
            abort(HTTPStatus.NOT_FOUND)

        response_data = []
        for airline_name, data in airlines_airports.items():
            airports_data = data.get("airports", [])

            response_data.append({
                "airline_name": airline_name,
                "airports": [
                    airport.put_into_dto() if hasattr(airport, 'put_into_dto') else airport
                    for airport in airports_data
                ] if airports_data else []
            })
        # print(response_data)
        return response_data

    def link_airline_to_airport(self, airline_name, airport_ICAO):
        return self._service.link_airline_to_airport(airline_name, airport_ICAO)