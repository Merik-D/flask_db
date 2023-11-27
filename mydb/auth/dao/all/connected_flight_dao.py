from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.all.connected_flight import ConnectedFlight


class ConnectedFlightDao(GeneralDAO):
    _domain_type = ConnectedFlight