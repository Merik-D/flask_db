from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.all.user_additional_info import UserAdditionalInfo


class UserAdditionalInfoDao(GeneralDAO):
    _domain_type = UserAdditionalInfo

    def insert_packet_of_user_additional_info(self):
        try:
            sql_statement = text("CALL insert_packet_of_user_additional_info()")
            self._session.execute(sql_statement)
            self._session.commit()
            return self.find_all()
        except OperationalError as e:
            print(f"Error executing stored procedure: {e}")
            return None