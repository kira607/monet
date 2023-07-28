# mypy: disable-error-code="name-defined,no-redef,assignment"

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from monet.orm import db


class BlocklistToken(db.Model):
    """A blocklisted token that has beed revoked."""

    __tablename__ = "blocklist_token"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    jti: Mapped[str] = mapped_column(db.String(36), nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
