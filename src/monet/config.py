"""Config settings for for development, testing and production environments."""
import os
from datetime import timedelta
from typing import Literal

ConfigName = Literal["development", "testing", "production"]
DEFAULT_SECRET: str = "Hello there! General Kenobi!"
DEFAULT_TOKEN_EXPIRE_HOURS: int = 24 * 7
DEFAULT_TOKEN_EXPIRE_MINUTES: int = 0


class Config:
    """Base configuration."""

    # Flask - https://flask.palletsprojects.com/en/2.3.x/config/

    SECRET_KEY = os.getenv("SECRET_KEY", DEFAULT_SECRET)
    PRESERVE_CONTEXT_ON_EXCEPTION: bool | None = True
    EXPLAIN_TEMPLATE_LOADING = False
    SESSION_COOKIE_SAMESITE = "Lax"
    PROPAGATE_EXCEPTIONS = True

    TESTING = False
    DEBUG = False

    # Auth & stuff

    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRE_HOURS = 0
    TOKEN_EXPIRE_MINUTES = 0
    SWAGGER_UI_DOC_EXPANSION = "list"
    RESTX_MASK_SWAGGER = False
    JSON_SORT_KEYS = False

    # flask-jwt-extended

    JWT_ERROR_MESSAGE_KEY = "message"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta()

    # Flask-SQLAlchemy

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:  # noqa: N802
        """Get a database uri."""
        return (
            f"{self.DB_DIALECT}"
            f"+{self.DB_DRIVER}"
            f"://{self.DB_USERNAME}"
            f":{self.DB_PASSWORD}"
            f"@{self.DB_HOSTNAME}"
            f"/{self.DB_NAME}"
        )

    # Logging

    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")

    # Deployment

    DEPLOY_SECRET_KEY = os.getenv("DEPLOY_SECRET_KEY", DEFAULT_SECRET)

    # Database

    DB_DIALECT = os.getenv("DB_DIALECT", "mysql")
    DB_DRIVER = os.getenv("DB_DRIVER", "pymysql")
    DB_USERNAME = os.getenv("DB_USERNAME", "kirill")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "kirill")
    DB_HOSTNAME = os.getenv("DB_HOSTNAME", "127.0.0.1")
    DB_NAME = os.getenv("DB_NAME", "monet_dev")

    # Google OAuth

    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", DEFAULT_SECRET)
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", DEFAULT_SECRET)


class DevelopmentConfig(Config):
    """Development configuration."""

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    DEBUG = True
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=5)

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:  # noqa: N802
        """Get a database uri."""
        return "sqlite:///:memory:"


class ProductionConfig(Config):
    """Production configuration."""

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)
    BCRYPT_LOG_ROUNDS = 13
    PRESERVE_CONTEXT_ON_EXCEPTION = None


_ENV_CONFIG_DICT = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


def get_config(config_name: ConfigName) -> Config:
    """
    Get environment configuration settings.

    :param config_name: Name of the config (should correspond to FLASK_ENV).
    :return: A configuration object for the Flask app.
    """
    return _ENV_CONFIG_DICT.get(config_name, ProductionConfig)()
