from datetime import datetime
from sqlalchemy.orm import (
    Mapped, 
    mapped_column
)

from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    date_create: Mapped[datetime] = mapped_column(
        default=datetime.now()
    )