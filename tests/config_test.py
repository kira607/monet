"""Unit tests for environment config settings."""

import os
from datetime import timedelta

import pytest

from monet.app import create_app
from monet.config import DEFAULT_SECRET


@pytest.mark.skipif(os.getenv("SECRET_KEY") is None, reason="environment is not set")
def test_config_development() -> None:
    """Test config settings for development environment."""
    app = create_app("development")
    assert app.config["SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["DEPLOY_SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_ID"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_SECRET"] != DEFAULT_SECRET
    assert app.config["TESTING"] is False
    assert app.config["DEBUG"] is True
    assert app.config["JWT_ACCESS_TOKEN_EXPIRES"] == timedelta(minutes=15)


@pytest.mark.skipif(os.getenv("SECRET_KEY") is None, reason="environment is not set")
def test_config_testing() -> None:
    """Test config settings for testing environment."""
    app = create_app("testing")
    assert app.config["SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["DEPLOY_SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_ID"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_SECRET"] != DEFAULT_SECRET
    assert app.config["TESTING"] is True
    assert app.config["DEBUG"] is True
    assert app.config["JWT_ACCESS_TOKEN_EXPIRES"] == timedelta(seconds=5)


@pytest.mark.skipif(os.getenv("SECRET_KEY") is None, reason="environment is not set")
def test_config_production() -> None:
    """Test config settings for production environment."""
    app = create_app("production")
    assert app.config["SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["DEPLOY_SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_ID"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_SECRET"] != DEFAULT_SECRET
    assert app.config["TESTING"] is False
    assert app.config["DEBUG"] is False
    assert app.config["JWT_ACCESS_TOKEN_EXPIRES"] == timedelta(hours=12)
