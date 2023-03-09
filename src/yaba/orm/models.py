from typing import List

from flask_login import UserMixin
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash

from yaba.orm import db


class User(db.Model, UserMixin):  # type: ignore
    '''A user.'''

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    username: Mapped[str] = mapped_column(String(50))
    name: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(102))

    def check_password(self, other_password) -> bool:
        return check_password_hash(self.password, other_password)

    def __repr__(self) -> str:
        '''Get a class repr.'''
        return f'User(id={self.id!r}, username={self.name!r})'
