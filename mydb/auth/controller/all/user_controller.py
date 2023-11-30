from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import user_service


class UserController(GeneralController):
    _service = user_service