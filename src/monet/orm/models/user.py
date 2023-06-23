# mypy: disable-error-code="name-defined,no-redef"

import uuid

from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column

from monet.orm import db


class User(db.Model, UserMixin):
    """A user."""

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003
    public_id: Mapped[str] = mapped_column(
        db.String(36),
        unique=True,
        default=lambda: str(uuid.uuid4()),
    )
    email: Mapped[str] = mapped_column(db.String(80), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    name: Mapped[str] = mapped_column(db.String(50), nullable=True)
    events: Mapped[list["UserEvent"]] = db.relationship(back_populates="user")  # noqa: F821
    roles = db.relationship(
        "Role",
        secondary="roles_users",
        backref=db.backref("users", lazy="dynamic"),
    )

    def __repr__(self) -> str:
        """Get a class repr."""
        return f"User(id={self.id!r}, email={self.email!r})"
