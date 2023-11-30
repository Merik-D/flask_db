from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer
from mydb import db
from mydb.auth.domain.i_dto import IDto

class User(IDto, db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    surname = Column(String(45), nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, surname={self.surname})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> User:
        obj = User(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
        }
