
import os
from typing import Any, Callable


class ConfigField:
    '''
    A config object field descriptor.

    :param value: A field default value.
    :param env: If true, upon name set descriptor will try to
      find an environment variable with the same name.
    :param env_name: A name of the environment variable to find.
    :param cast: A callable executed on value on each set (basically validator).
    :param secret: If true, value won't show up in __str__ of :class:`YabaConfig`.
    '''

    def __init__(
        self,
        value: Any = None,
        *,
        env: bool = True,
        env_name: str | None = None,
        cast: Callable[[Any], Any] = str,
        secret: bool = False,
    ) -> None:
        self._value = value
        self._env = env
        self._env_name = env_name
        self._cast = cast
        self._secret = secret

    def __set_name__(self, owner: type['YabaConfig'], name: str) -> None:
        self._name = name
        self._env_name = self._env_name or self._name
        fields = owner._fields
        fields.append(self)
        if self._env:
            self.value = os.getenv(self._env_name)

    def __set__(self, obj: object, value: Any) -> None:
        raise RuntimeError('Cannot assign config value')

    def __get__(self, obj: object, objtype: type['YabaConfig']) -> Any:
        if obj is None:
            return self
        return self.value

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value: Any) -> Any:
        self._value = self._cast(value)

    @property
    def is_secret(self) -> bool:
        return self._secret


def validate_bool_field(value: str | None) -> bool:
    if value is None:
        return False
    return value.lower() in ('true', '1')


class YabaConfig:
    '''
    A yaba config object.

    This object is passed to an app instance.
    '''

    _fields: list[ConfigField] = []

    # Flask
    FLASK_APP = ConfigField()
    EXPLAIN_TEMPLATE_LOADING = ConfigField(cast=validate_bool_field)
    FLASK_DEBUG = ConfigField(cast=validate_bool_field)
    # Logging
    LOGGING_LEVEL = ConfigField()
    # Secrets
    SECRET_KEY = ConfigField(secret=True)
    DEPLOY_SECRET_KEY = ConfigField(secret=True)
    SECURITY_PASSWORD_SALT = ConfigField(secret=True)
    # Database
    DB_DIALECT = ConfigField()
    DB_DRIVER = ConfigField()
    DB_USERNAME = ConfigField(secret=True)
    DB_PASSWORD = ConfigField(secret=True)
    DB_HOSTNAME = ConfigField(secret=True)
    DB_NAME = ConfigField(secret=True)
    SQLALCHEMY_DATABASE_URI = ConfigField(env=False, secret=True)
    # Google OAuth
    GOOGLE_CLIENT_ID = ConfigField(secret=True)
    GOOGLE_CLIENT_SECRET = ConfigField(secret=True)

    def __init__(self) -> None:
        self.__class__.SQLALCHEMY_DATABASE_URI.value = (
            f'{self.DB_DIALECT}'
            f'+{self.DB_DRIVER}'
            f'://{self.DB_USERNAME}'
            f':{self.DB_PASSWORD}'
            f'@{self.DB_HOSTNAME}'
            f'/{self.DB_NAME}'
        )

    def __str__(self) -> str:
        '''
        Get a string representation of config.

        Creates a string in format 'name1=value1, name2=value2, ...'

        If field is secret and app is not in debug mode,
        it value is replaced with #SECRET# string
        for purpose of security.
        '''
        fs = []

        for field in self._fields:
            value = repr(field.value) if self.FLASK_DEBUG or not field.is_secret else '#SECRET#'
            fs.append(f'{field.name}={value} ({type(field.value)})')

        fields_string = ', '.join(fs)
        return f'{self.__class__.__name__}({fields_string})'