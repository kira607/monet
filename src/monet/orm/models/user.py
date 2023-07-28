# mypy: disable-error-code="name-defined,no-redef,assignment"

import typing

from sqlalchemy.orm import Mapped, mapped_column

from monet.orm import db

if typing.TYPE_CHECKING:
    from monet.orm.models import Role, UserEvent


class User(db.Model):
    """A user."""

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    email: Mapped[str] = mapped_column(db.String(80), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)

    fisrt_name: Mapped[str | None] = mapped_column(db.String(50))
    last_name: Mapped[str | None] = mapped_column(db.String(50))

    events: Mapped[list["UserEvent"]] = db.relationship(back_populates="user")  # noqa: F821
    roles: Mapped[list["Role"]] = db.relationship(secondary="user_has_role", back_populates="users")

    def __repr__(self) -> str:
        """Get a class repr."""
        return f"User(id={self.id!r}, email={self.email!r})"
