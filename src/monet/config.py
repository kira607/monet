"""Config settings for for development, testing and production environments."""
import os
from datetime import timedelta
from typing import Literal

ConfigName = Literal["dev", "test", "prod"]
DEFAULT_SECRET = "Hello there! General Kenobi!"


class Config:
    """Base configuration."""

    # Flask - https://flask.palletsprojects.com/en/2.3.x/config/

    FLASK_APP = "src/monet.app:create_app()"
    SECRET_KEY = os.getenv("SECRET_KEY", DEFAULT_SECRET)
    PRESERVE_CONTEXT_ON_EXCEPTION: bool | None = True
    EXPLAIN_TEMPLATE_LOADING = False
    SESSION_COOKIE_SAMESITE = "Lax"

    TESTING = False
    DEBUG = False

    # Auth & stuff

    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRE_HOURS = 0
    TOKEN_EXPIRE_MINUTES = 0
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = "list"
    RESTX_MASK_SWAGGER = False
    JSON_SORT_KEYS = False

    # Flask-SQLAlchemy

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

    # Flask-Login - https://flask-login.readthedocs.io/en/latest/#configuring-your-application

    # The name of the cookie to store the “remember me” information in
    REMEMBER_COOKIE_NAME = "remember_token"
    # The amount of time before the cookie expires, as a datetime.timedelta object or integer seconds
    REMEMBER_COOKIE_DURATION = timedelta(days=365)
    # If the “Remember Me” cookie should cross domains, set the domain value here
    # (i.e. .example.com would allow the cookie to be used on all subdomains of example.com)
    REMEMBER_COOKIE_DOMAIN = None
    # Limits the “Remember Me” cookie to a certain path
    REMEMBER_COOKIE_PATH = "/"
    # Restricts the “Remember Me” cookie’s scope to secure channels (typically HTTPS)
    REMEMBER_COOKIE_SECURE = False
    # Prevents the “Remember Me” cookie from being accessed by client-side scripts
    REMEMBER_COOKIE_HTTPONLY = True
    # If set to True the cookie is refreshed on every request,
    # which bumps the lifetime. Works like Flask’s SESSION_REFRESH_EACH_REQUEST
    REMEMBER_COOKIE_REFRESH_EACH_REQUEST = False
    # Restricts the “Remember Me” cookie to first-party or same-site context
    REMEMBER_COOKIE_SAMESITE = None

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

    TOKEN_EXPIRE_MINUTES = 15
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True


class ProductionConfig(Config):
    """Production configuration."""

    TOKEN_EXPIRE_HOURS = 1
    BCRYPT_LOG_ROUNDS = 13
    PRESERVE_CONTEXT_ON_EXCEPTION = None


_ENV_CONFIG_DICT = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig,
}


def get_config(config_name: ConfigName) -> Config:
    """Retrieve environment configuration settings."""
    return _ENV_CONFIG_DICT.get(config_name, ProductionConfig)()
