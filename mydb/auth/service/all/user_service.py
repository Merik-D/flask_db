from mydb.auth.dao import user_dao
from mydb.auth.service.general_service import GeneralService


class UserService(GeneralService):
    _dao = user_dao