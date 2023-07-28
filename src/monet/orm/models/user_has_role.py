# mypy: disable-error-code="name-defined,no-redef,assignment"

from sqlalchemy.orm import Mapped, mapped_column

from monet.orm import db


class UserHasRole(db.Model):
    """A secondary table for establishing many-to-many relationship between users and roles."""

    __tablename__ = "user_has_role"

    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"), primary_key=True)
    role_id: Mapped[int] = mapped_column(db.ForeignKey("role.id"), primary_key=True)
