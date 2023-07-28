import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import CreateSchema

from monet.app import create_app
from monet.orm import db as database
from monet.orm.models import User
from tests.utils import EMAIL, PASSWORD


@pytest.fixture
def app() -> Flask:
    """Get an app instance with testing configuration."""
    app = create_app("testing")
    app.testing = True
    app.test_client()
    return app


def create_schema_if_not_exists(database: SQLAlchemy, schema_name: str) -> None:
    """Create a schema if not exists.

    :param database: SQLAlchemy database.
    :param schema_name: Name of the schema.
    :return: None
    """
    engine = database.engine
    conn = engine.connect()
    if not engine.dialect.has_schema(conn, schema_name):
        engine.execute(CreateSchema(schema_name))  # type: ignore [no-untyped-call]


@pytest.fixture
def db(app: Flask, client: FlaskClient, request: pytest.FixtureRequest) -> SQLAlchemy:
    """Get a database instance.

    :param app: Flask app instance.
    :param client: Flask testing client instance.
    :param request: ???
    :return: Flask-SQLAlchemy instance.
    """
    database.drop_all()
    database.create_all()
    database.session.commit()

    def fin() -> None:
        database.session.remove()

    request.addfinalizer(fin)
    return database


@pytest.fixture
def user(db: SQLAlchemy) -> User:
    """Get a testing :class:`monet.orm.models.User` instance.

    :param db: A testing database instance.
    """
    user = User(email=EMAIL, password=PASSWORD)
    db.session.add(user)
    db.session.commit()
    return user
