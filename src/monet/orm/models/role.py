# mypy: disable-error-code="name-defined,no-redef,assignment"

import typing

from sqlalchemy.orm import Mapped, mapped_column

from monet.orm import db

if typing.TYPE_CHECKING:
    from monet.orm.models import User


class Role(db.Model):
    """A user role."""

    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003
    name: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(db.Text())

    users: Mapped[list["User"]] = db.relationship(
        secondary="user_has_role",
        back_populates="roles",
    )
