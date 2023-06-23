# mypy: disable-error-code="name-defined,no-redef"

import datetime
from enum import Enum

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from monet.orm import db


class UserEventType(Enum):
    """A user event."""

    REGISTER = "register"
    LOGIN = "login"
    LOG_OUT = "log out"
    PASSWORD_CHANGE = "password_change"
    EDIT = "edit"


class UserEvent(db.Model):
    """Events happened to user account."""

    __tablename__ = "user_event"

    # Just PK
    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    # Monitoring stuff (for future metrics and debugging)
    event_type: Mapped[UserEventType] = mapped_column()

    date_time: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    ip: Mapped[str] = mapped_column(db.String(100), nullable=True)
    email: Mapped[str | None] = mapped_column(db.String(80))
    password: Mapped[str | None] = mapped_column(db.String(255))

    # Stuff
    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    user: Mapped["User"] = db.relationship(back_populates="events")  # noqa: F821
