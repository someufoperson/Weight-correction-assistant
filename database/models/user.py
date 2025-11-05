from sqlalchemy import BigInteger, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.database import Base

import enum

class Gender(enum.Enum):
    male = "male"
    female = "female"

class UserOrm(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    age: Mapped[int]
    desired_weight: Mapped[float]
    gender: Mapped[Gender]
    undesirable_products: Mapped[str] = mapped_column(String(length=1024))
    preferred_products: Mapped[str] = mapped_column(String(length=1024))
    # correction_program: Mapped["correction_programm"] = relationship()