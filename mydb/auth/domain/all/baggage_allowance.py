from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from mydb import db
from mydb.auth.domain.i_dto import IDto

class BaggageAllowance(IDto, db.Model):
    __tablename__ = "baggage_allowance"

    id = Column(Integer, primary_key=True)
    max_weight = Column(Integer, nullable=False)
    max_side = Column(Integer, nullable=False)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)

    flight = relationship("Flight", back_populates="baggage_allowance")

    def __repr__(self):
        return f"BaggageAllowance(id={self.id}, max_weight={self.max_weight}, max_side={self.max_side}, flight_id={self.flight_id})"

    def put_into_dto(self) -> dict[str, any]:
        return {
            "id": self.id,
            "max_weight": self.max_weight,
            "max_side": self.max_side,
            "flight_id": self.flight_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, any]) -> 'Baggage':
        obj = BaggageAllowance(
            id=dto_dict.get("id"),
            max_weight=dto_dict.get("max_weight"),
            max_side=dto_dict.get("max_side"),
            flight_id=dto_dict.get("flight_id"),
        )
        return obj