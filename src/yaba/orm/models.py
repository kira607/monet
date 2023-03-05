from typing import List, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from yaba.orm import db


class User(db.Model):  # type: ignore
    '''A user.'''

    __tablename__ = 'user_account'

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]] = mapped_column(String(60))
    addresses: Mapped[List['Address']] = relationship(back_populates='user')

    def __repr__(self) -> str:
        '''Get a class repr.'''
        return f'User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})'


class Address(db.Model):  # type: ignore
    '''An email address related to user.'''

    __tablename__ = 'address'

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003
    email_address: Mapped[str] = mapped_column(String(50))
    user_id = mapped_column(ForeignKey('user_account.id'))
    user: Mapped[User] = relationship(back_populates='addresses')

    def __repr__(self) -> str:
        '''Get a class repr.'''
        return f'Address(id={self.id!r}, email_address={self.email_address!r})'
