from sqlalchemy import Column, Integer, Float, ForeignKey, Index
from sqlalchemy.orm import relationship
from mydb import db
from mydb.auth.domain.i_dto import IDto

class Ticket(IDto, db.Model):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    seat_number = Column(Integer, nullable=False, info={'unsigned': True})
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)

    flight = relationship("Flight", back_populates="tickets")

    Index('fk_ticket_flight1_idx', 'flight_id')

    def __repr__(self):
        return f"Ticket(id={self.id}, price={self.price}, seat_number={self.seat_number}, flight_id={self.flight_id})"

    def put_into_dto(self) -> dict[str, any]:
        return {
            "id": self.id,
            "price": self.price,
            "seat_number": self.seat_number,
            "flight_id": self.flight_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, any]) -> 'Ticket':
        obj = Ticket(
            id=dto_dict.get("id"),
            price=dto_dict.get("price"),
            seat_number=dto_dict.get("seat_number"),
            flight_id=dto_dict.get("flight_id"),
        )
        return obj
