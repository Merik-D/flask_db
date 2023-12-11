from mydb.auth.dao.all.airline_dao import AirlineDao
from mydb.auth.dao.all.airport_dao import AirportDao
from mydb.auth.dao.all.baggage_allowance_dao import BaggageAllowanceDao
from mydb.auth.dao.all.connected_flight_dao import ConnectedFlightDao
from mydb.auth.dao.all.flight_dao import FlightDao
from mydb.auth.dao.all.ticket_dao import TicketDao
from mydb.auth.dao.all.ticket_purchase_history_dao import TicketPurchaseHistoryDao
from mydb.auth.dao.all.user_additional_info_dao import UserAdditionalInfoDao
from mydb.auth.dao.all.user_dao import UserDao

airline_dao = AirlineDao()
airport_dao = AirportDao()
baggage_allowance_dao = BaggageAllowanceDao()
connected_flight_dao = ConnectedFlightDao()
flight_dao = FlightDao()
ticket_dao = TicketDao()
ticket_purchase_history_dao = TicketPurchaseHistoryDao()
user_dao = UserDao()
user_additional_info_dao = UserAdditionalInfoDao()