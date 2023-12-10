from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto

class UserAdditionalInfo(IDto, db.Model):
    __tablename__ = "user_additional_info"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    additional_info = Column(String(255), nullable=False)

    user = relationship("User", back_populates="additional_info")

    def __repr__(self):
        return f"UserAdditionalInfo(user_id={self.user_id}, additional_info={self.additional_info})"

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "user_id": self.user_id,
            "additional_info": self.additional_info,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> 'UserAdditionalInfo':
        obj = UserAdditionalInfo(
            user_id=dto_dict.get("user_id"),
            additional_info=dto_dict.get("additional_info"),
        )
        return obj
