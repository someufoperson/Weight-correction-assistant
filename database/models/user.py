from sqlalchemy import BigInteger, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.sql import func

from database.database import Base

import enum
import datetime

class Gender(enum.Enum):
    male = "male"
    female = "female"

class Language(enum.Enum):
    russian = "russian"
    english = "english"

class UserOrm(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=64))
    age: Mapped[int]
    actual_weight: Mapped[float]
    height = Mapped[int]
    desired_weight: Mapped[float]
    gender: Mapped[Gender]
    undesirable_products: Mapped[str] = mapped_column(String(length=1024))
    preferred_products: Mapped[str] = mapped_column(String(length=1024))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    lang: Mapped[Language]
    # correction_program: Mapped["correction_programm"] = relationship()