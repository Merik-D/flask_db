from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.all.flight import Flight


class FlightDao(GeneralDAO):
    _domain_type = Flight