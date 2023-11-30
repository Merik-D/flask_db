from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, Index
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.all.airline import airline_airport_association
from mydb.auth.domain.all.flight import flight_airport_association
from mydb.auth.domain.i_dto import IDto

class Airport(IDto, db.Model):
    __tablename__ = "airport"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ICAO = Column(String(4), nullable=False)
    city = Column(String(45), nullable=False)

    airlines = relationship("Airline", secondary=airline_airport_association, back_populates="airports")
    flights = relationship("Flight", secondary=flight_airport_association, back_populates="airports")


    departing_flights = relationship("Flight", foreign_keys="Flight.departure_airport_id",
                                     back_populates="departure_airport")

    arriving_flights = relationship("Flight", foreign_keys="Flight.arrival_airport_id",
                                    back_populates="arrival_airport")

    def __repr__(self):
        return f"Airport(id={self.id}, ICAO={self.ICAO}, city={self.city})"

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "ICAO": self.ICAO,
            "city": self.city,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> 'Airport':
        obj = Airport(
            id=dto_dict.get("id"),
            ICAO=dto_dict.get("ICAO"),
            city=dto_dict.get("city"),
        )
        return obj