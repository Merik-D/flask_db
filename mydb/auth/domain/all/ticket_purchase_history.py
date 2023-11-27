from sqlalchemy import Column, Integer, ForeignKey
from mydb import db
from mydb.auth.domain.i_dto import IDto

class TicketPurchaseHistory(IDto, db.Model):
    __tablename__ = "ticket_purchase_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    ticket_id = Column(Integer, ForeignKey('ticket.id'), nullable=False)

    def __repr__(self):
        return f"TicketPurchaseHistory(id={self.id}, user_id={self.user_id}, ticket_id={self.ticket_id})"

    def put_into_dto(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "ticket_id": self.ticket_id,
        }

    @staticmethod
    def create_from_dto(dto_dict):
        return TicketPurchaseHistory(
            id=dto_dict.get("id"),
            user_id=dto_dict.get("user_id"),
            ticket_id=dto_dict.get("ticket_id"),
        )
