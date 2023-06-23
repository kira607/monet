"""Unit tests for environment config settings."""
from monet.app import create_app
from monet.config import DEFAULT_SECRET


def test_config_development() -> None:
    """Test config settings for development environment."""
    app = create_app("dev")
    assert app.config["SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["DEPLOY_SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_ID"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_SECRET"] != DEFAULT_SECRET
    assert not app.config["TESTING"]
    assert app.config["TOKEN_EXPIRE_HOURS"] == 0
    assert app.config["TOKEN_EXPIRE_MINUTES"] == 15


def test_config_testing() -> None:
    """Test config settings for testing environment."""
    app = create_app("test")
    assert app.config["SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["DEPLOY_SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_ID"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_SECRET"] != DEFAULT_SECRET
    assert app.config["TESTING"]
    assert app.config["TOKEN_EXPIRE_HOURS"] == 0
    assert app.config["TOKEN_EXPIRE_MINUTES"] == 0


def test_config_production() -> None:
    """Test config settings for production environment."""
    app = create_app("prod")
    assert app.config["SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["DEPLOY_SECRET_KEY"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_ID"] != DEFAULT_SECRET
    assert app.config["GOOGLE_CLIENT_SECRET"] != DEFAULT_SECRET
    assert not app.config["TESTING"]
    assert app.config["TOKEN_EXPIRE_HOURS"] == 1
    assert app.config["TOKEN_EXPIRE_MINUTES"] == 0
