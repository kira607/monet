# mypy: disable-error-code="name-defined,no-redef"

from sqlalchemy.orm import Mapped, mapped_column

from monet.orm import db


class RolesUsers(db.Model):
    """A secondary table for establishing many-to-many relationship between users and roles."""

    __tablename__ = "roles_users"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    user_id = db.Column("user_id", db.Integer(), db.ForeignKey("user.id"))
    role_id = db.Column("role_id", db.Integer(), db.ForeignKey("role.id"))
