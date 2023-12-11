from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import user_additional_info_service


class UserAdditionalInfoController(GeneralController):
    _service = user_additional_info_service

    def insert_packet_of_user_additional_info(self):
        return self._service.insert_packet_of_user_additional_info()