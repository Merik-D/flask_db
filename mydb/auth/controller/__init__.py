from mydb.auth.controller.all.airline_controller import AirlineController
from mydb.auth.controller.all.airport_controller import AirportController
from mydb.auth.controller.all.baggage_allowance_controller import BaggageAllowanceController
from mydb.auth.controller.all.connected_flight_controller import ConnectedFlightController
from mydb.auth.controller.all.flight_controller import FlightController
from mydb.auth.controller.all.ticket_controller import TicketController
from mydb.auth.controller.all.ticket_purchase_history_controller import TicketPurchaseHistoryController
from mydb.auth.controller.all.user_controller import UserController

airline_controller = AirlineController()
airport_controller = AirportController()
baggage_allowance_controller = BaggageAllowanceController()
connected_flight_controller = ConnectedFlightController()
flight_controller = FlightController()
ticket_controller = TicketController()
ticket_purchase_history_controller = TicketPurchaseHistoryController()
user_controller = UserController()