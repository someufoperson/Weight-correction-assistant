from sqlalchemy import JSON, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

import enum
import datetime

class Type_of_correction(enum.Enum):
    weight_gain = "weight_gain"
    weight_loss = "weight_loss"

class Correction_programOrm(Base):
    __tablename__ = "correction_programs"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, 
                                    autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete="CASCADE"))
    is_active: Mapped[bool] = mapped_column(default=True, nullable=True)
    Type_of_correction: Mapped[Type_of_correction]
    content = mapped_column(JSON(none_as_null=True))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    # users: Mapped["users"]