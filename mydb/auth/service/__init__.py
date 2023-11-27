from mydb.auth.service.all.airline_service import AirlineService
from mydb.auth.service.all.airport_service import AirportService
from mydb.auth.service.all.baggage_allowance_service import BaggageAllowanceService
from mydb.auth.service.all.connected_flight_service import ConnectedFlightService
from mydb.auth.service.all.flight_service import FlightService
from mydb.auth.service.all.ticket_purchase_history_service import TicketPurchaseHistoryService
from mydb.auth.service.all.ticket_service import TicketService
from mydb.auth.service.all.user_service import UserService

airline_service = AirlineService()
airport_service = AirportService()
baggage_allowance_service = BaggageAllowanceService()
connected_flight_service = ConnectedFlightService()
flight_service = FlightService()
ticket_service = TicketService()
ticket_purchase_history_service = TicketPurchaseHistoryService()
user_service = UserService()