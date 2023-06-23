# mypy: disable-error-code="name-defined,no-redef"

from sqlalchemy.orm import Mapped, mapped_column

from monet.orm import db


class Role(db.Model):
    """A user role."""

    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003
    name: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(db.Text())
    users = db.relationship(
        "User",
        secondary="roles_users",
        backref=db.backref("roles", lazy="dynamic"),
    )
