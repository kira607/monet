from datetime import timedelta


class Config:
    '''A base configuration class.'''

    # Flask - https://flask.palletsprojects.com/en/2.3.x/config/

    FLASK_APP = 'src/yaba.app:create_app()'
    SECRET_KEY = 'a secret key'
    PRESERVE_CONTEXT_ON_EXCEPTION = True
    EXPLAIN_TEMPLATE_LOADING = False
    SESSION_COOKIE_SAMESITE = 'Lax'
    TESING = False
    DEBUG = True

    # Flask-Login - https://flask-login.readthedocs.io/en/latest/#configuring-your-application

    # The name of the cookie to store the “remember me” information in
    REMEMBER_COOKIE_NAME = 'remember_token'
    # The amount of time before the cookie expires, as a datetime.timedelta object or integer seconds
    REMEMBER_COOKIE_DURATION = timedelta(days=365)
    # If the “Remember Me” cookie should cross domains, set the domain value here
    # (i.e. .example.com would allow the cookie to be used on all subdomains of example.com)
    REMEMBER_COOKIE_DOMAIN = None
    # Limits the “Remember Me” cookie to a certain path
    REMEMBER_COOKIE_PATH = '/'
    # Restricts the “Remember Me” cookie’s scope to secure channels (typically HTTPS)
    REMEMBER_COOKIE_SECURE = False
    # Prevents the “Remember Me” cookie from being accessed by client-side scripts
    REMEMBER_COOKIE_HTTPONLY = True
    # If set to True the cookie is refreshed on every request,
    # which bumps the lifetime. Works like Flask’s SESSION_REFRESH_EACH_REQUEST
    REMEMBER_COOKIE_REFRESH_EACH_REQUEST = False
    # Restricts the “Remember Me” cookie to first-party or same-site context
    REMEMBER_COOKIE_SAMESITE = None

    # Flask-SQLAlchemy

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:  # noqa: N802, D102
        return (
            f'{self.DB_DIALECT}'
            f'+{self.DB_DRIVER}'
            f'://{self.DB_USERNAME}'
            f':{self.DB_PASSWORD}'
            f'@{self.DB_HOSTNAME}'
            f'/{self.DB_NAME}'
        )

    # Logging

    LOGGING_LEVEL = 'INFO'

    # Deployment

    DEPLOY_SECRET_KEY = 'git hub secret key'

    # Database

    DB_DIALECT = 'mysql'
    DB_DRIVER = 'pymysql'
    DB_USERNAME = 'kirill'
    DB_PASSWORD = 'kirill'
    DB_HOSTNAME = '127.0.0.1'
    DB_NAME = 'yaba'

    # Google OAuth

    GOOGLE_CLIENT_ID = 'google client id'
    GOOGLE_CLIENT_SECRET = 'google client secret'


class TestingConfig(Config):
    '''A config object for testing.'''

    TESING = True
