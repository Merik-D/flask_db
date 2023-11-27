from mydb.auth.dao import baggage_allowance_dao
from mydb.auth.service.general_service import GeneralService


class BaggageAllowanceService(GeneralService):
    _dao = baggage_allowance_dao