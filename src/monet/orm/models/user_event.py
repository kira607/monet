# mypy: disable-error-code="name-defined,no-redef,assignment"

import datetime
import typing
from enum import Enum

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from monet.orm import db

if typing.TYPE_CHECKING:
    from monet.orm.models import User


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

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    event_type: Mapped[UserEventType] = mapped_column()
    date_time: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    ip: Mapped[str] = mapped_column(db.String(100), nullable=True)

    email: Mapped[str | None] = mapped_column(db.String(80))
    password: Mapped[str | None] = mapped_column(db.String(255))
    fisrt_name: Mapped[str | None] = mapped_column(db.String(50))
    last_name: Mapped[str | None] = mapped_column(db.String(50))

    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    user: Mapped["User"] = db.relationship(back_populates="events")  # noqa: F821
