from mydb.auth.dao import user_additional_info_dao
from mydb.auth.service.general_service import GeneralService


class UserAdditionalInfoService(GeneralService):
    _dao = user_additional_info_dao

    def insert_packet_of_user_additional_info(self):
        return self._dao.insert_packet_of_user_additional_info()