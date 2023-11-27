from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


airline_airport_association = Table(
    'airline_airport', db.Model.metadata,
    Column('airline_id', Integer, ForeignKey('airline.id')),
    Column('airport_id', Integer, ForeignKey('airport.id'))
)

class Airline(IDto, db.Model):
    __tablename__ = "airline"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    country_registration = Column(String(45), nullable=False)

    airports = relationship("Airport", secondary=airline_airport_association, back_populates="airlines")

    def __repr__(self):
        return f"Airline(id={self.id}, name={self.name}, country_registration={self.country_registration})"

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "country_registration": self.country_registration,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> 'Airline':
        obj = Airline(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            country_registration=dto_dict.get("country_registration"),
        )
        return obj