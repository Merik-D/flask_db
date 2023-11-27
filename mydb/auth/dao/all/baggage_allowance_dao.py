from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.all.baggage_allowance import BaggageAllowance


class BaggageAllowanceDao(GeneralDAO):
    _domain_type = BaggageAllowance