from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from marshmallow import Schema
from marshmallow import fields
from marshmallow import validate
from marshmallow import post_load
from marshmallow import ValidationError
from marshmallow import INCLUDE

from yaba.logger import logger
from yaba.orm import db
from yaba.orm.models import User
from yaba.orm.models import UserEvent


class UserSchema(Schema):
    '''A user registration schema.'''

    class Meta:
        unknown = INCLUDE

    __model__ = User

    email = fields.Email(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False, load_only=True, validate=validate.Length(min=8))
    password_confirm = fields.Str(required=True, allow_none=False, load_only=True, validate=validate.Length(min=8))

    @post_load
    def make_user(self, data, **kwargs):
        if data['password'] != data['password_confirm']:
            raise ValidationError('Passwords dot not match')
        user = User(email=data['email'], password=data['password'])
        return user


class UserController:
    '''An user app controller.'''

    def register_user(self):
        logger.info('Registration')
        logger.info(f'IP: {request.remote_addr}')
        logger.info(f'form: {request.form}')
        try:
            user = UserSchema().load(request.form)
            logger.info(f'Created user: {user} ({user.password})')

            if User.query.filter_by(email=user.email).first():
                flash('User with given email already exists')
                return redirect(url_for('user.register'))

            flash('Registration successful!', 'success')
            return redirect(url_for('user.login'))
        except ValidationError as e:
            flash(f'{e}')
            return redirect(url_for('user.register'))
