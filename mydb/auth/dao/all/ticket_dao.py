from sqlalchemy import text

from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.all.ticket import Ticket


class TicketDao(GeneralDAO):
    _domain_type = Ticket

    def create(self, obj: object):
        self._session.execute(
            text("CALL insert_ticket(:price, :seat_number, :flight_id)"),
            {"price": obj.price, "seat_number": obj.seat_number,
             "flight_id": obj.flight_id}
        )
        self._session.commit()
        return obj

    def get_ticket_price_statistics(self, aggregate_type: str):
        return self._session.execute(text(f"CALL get_ticket_price_statistics('{aggregate_type}')")).all()