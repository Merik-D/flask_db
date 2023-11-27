from sqlalchemy import Column, Integer, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from mydb import db
from mydb.auth.domain.i_dto import IDto


flight_airport_association = Table(
    'airport_flight', db.Model.metadata,
    Column('airport_id', Integer, ForeignKey('airport.id')),
    Column('flight_id', Integer, ForeignKey('flight.id'))
)

class Flight(IDto, db.Model):
    __tablename__ = "flight"

    id = Column(Integer, primary_key=True, autoincrement=True)
    departure_airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    arrival_airport_id = Column(Integer, ForeignKey('airport.id'), nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)

    airports = relationship("Airport", secondary=flight_airport_association, back_populates="flights")

    departure_airport = relationship("Airport", foreign_keys=[departure_airport_id], back_populates="departing_flights")
    arrival_airport = relationship("Airport", foreign_keys=[arrival_airport_id], back_populates="arriving_flights")

    connected_flights1 = relationship("ConnectedFlight", foreign_keys="ConnectedFlight.flight1_id",
                                      back_populates="flight1")
    connected_flights2 = relationship("ConnectedFlight", foreign_keys="ConnectedFlight.flight2_id",
                                      back_populates="flight2")

    tickets = relationship("Ticket", back_populates="flight")
    baggage_allowance = relationship("BaggageAllowance", back_populates="flight")

    def __repr__(self):
        return f"Flight(id={self.id}, departure_airport_id={self.departure_airport_id}, arrival_airport_id={self.arrival_airport_id}, departure_time={self.departure_time}, arrival_time={self.arrival_time})"

    def put_into_dto(self) -> dict[str, any]:
        return {
            "id": self.id,
            "departure_airport_id": self.departure_airport_id,
            "arrival_airport_id": self.arrival_airport_id,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, any]) -> 'Flight':
        obj = Flight(
            id=dto_dict.get("id"),
            departure_airport_id=dto_dict.get("departure_airport_id"),
            arrival_airport_id=dto_dict.get("arrival_airport_id"),
            departure_time=dto_dict.get("departure_time"),
            arrival_time=dto_dict.get("arrival_time"),
        )
        return obj