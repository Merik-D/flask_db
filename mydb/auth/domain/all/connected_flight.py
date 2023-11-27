from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from mydb import db
from mydb.auth.domain.i_dto import IDto

class ConnectedFlight(IDto, db.Model):
    __tablename__ = "connected_flight"

    id = Column(Integer, primary_key=True, autoincrement=True)
    flight1_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    flight2_id = Column(Integer, ForeignKey('flight.id'), nullable=False)

    flight1 = relationship("Flight", foreign_keys=[flight1_id], back_populates="connected_flights1")
    flight2 = relationship("Flight", foreign_keys=[flight2_id], back_populates="connected_flights2")

    def __repr__(self):
        return f"ConnectedFlight(id={self.id}, flight1_id={self.flight1_id}, flight2_id={self.flight2_id})"

    def put_into_dto(self) -> dict[str, any]:
        return {
            "id": self.id,
            "flight1_id": self.flight1_id,
            "flight2_id": self.flight2_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, any]) -> 'ConnectedFlight':
        obj = ConnectedFlight(
            id=dto_dict.get("id"),
            flight1_id=dto_dict.get("flight1_id"),
            flight2_id=dto_dict.get("flight2_id"),
        )
        return obj
