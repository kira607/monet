# mypy: disable-error-code="name-defined,no-redef"

import datetime
from enum import Enum

from flask_login import UserMixin
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from yaba.orm import db


__all__ = [
    'User',
    'UserEvent',
    'UserEventType',
    'Role',
]


class RolesUsers(db.Model):
    '''A secondary table for establishing many-to-many relationship between users and roles.'''

    __tablename__ = 'roles_users'

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))


class Role(db.Model):
    '''A user role.'''

    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    name: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(db.Text())


class User(db.Model, UserMixin):
    '''A user.'''

    __tablename__ = 'user'

    # Just PK
    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    # Mandatory personal info
    email: Mapped[str] = mapped_column(db.String(80), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)

    # Optional personal info
    name: Mapped[str] = mapped_column(db.String(50), nullable=True)

    # Stuff
    events: Mapped[list['UserEvent']] = db.relationship(back_populates='user')
    roles = db.relationship(
        'Role',
        secondary='roles_users',
        backref=db.backref('users', lazy='dynamic'),
    )

    def __repr__(self) -> str:
        '''Get a class repr.'''
        return f'User(id={self.id!r}, email={self.email!r})'


class UserEventType(Enum):
    '''A user event.'''

    REGISTER = 'register'
    LOGIN = 'login'
    LOG_OUT = 'log out'
    PASSWORD_CHANGE = 'password_change'
    EDIT = 'edit'


class UserEvent(db.Model):
    '''Events happened to user account.'''

    __tablename__ = 'user_event'

    # Just PK
    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    # Monitoring stuff (for future metrics and debugging)
    event_type: Mapped[UserEventType] = mapped_column()

    date_time: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    ip: Mapped[str] = mapped_column(db.String(100), nullable=True)
    email: Mapped[str | None] = mapped_column(db.String(80))
    password: Mapped[str | None] = mapped_column(db.String(255))

    # Stuff
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    user: Mapped['User'] = db.relationship(back_populates='events')
