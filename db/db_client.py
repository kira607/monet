from contextlib import contextmanager
from typing import List, Union, Optional, Tuple, Iterable

from sqlalchemy import create_engine, Column
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeMeta

from db.models import Base


class DbClient:
    '''
    Client for SQLite database
    '''

    def __init__(self, storage_path: str):
        '''
        :param str storage_path: path to the storage file.db
        '''
        self.__storage_path = storage_path
        self.__engine = self.__create_engine()
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.session = scoped_session(session_factory)
        self.__create_tables()

    def quick_insert(self, model_type: Base, kwargs: dict) -> Base:
        '''
        Insert a new model in the database.

        Dynamically creates a new model and fills it with the parameters passed via kwargs.
        All unspecified parameters are filled by default (if default value is present).

        :param model_type: Model to create
        :param kwargs: parameters to be passed to the new model
        :return: inserted model
        '''
        model = model_type(**kwargs)
        with self.session() as session:
            session.add(model)
        return model

    def insert(self, model: Base) -> Base:
        '''
        Insert ``model`` in the database

        :param model: Model to insert
        :return: inserted model
        '''
        with self.session() as session:
            session.add(model)
        return model

    def get(
        self,
        *entities: Union[Base, DeclarativeMeta, Column],
        filters: Tuple = (),
        limit: Optional[int] = None,
    ) -> Union[List[Base], Base]:
        '''
        Query entities in the database

        :param entities: Entities to be queried (columns or tables)
        :param filters: Filters to be applied to the query
        :param limit: Limit the number of entities to be returned.
         If limit=1: returns the entity itself. >
         If limit=N: returns N entities.
         If limit=None: returns all entities.
        :raises ValueError: If limit is &lt;= 0.
        :return: Query result
        '''
        if limit and limit <= 0:
            raise ValueError('limit must be positive')

        with self.session() as session:
            result = session.query(*entities)

        for filter_ in filters:
            if filter_ is not None:
                result = result.filter(filter_)

        if limit is None:
            return result.all()
        elif limit == 1:
            return result.first()
        else:
            return result.limit(limit).all()

    def update(
        self,
        model: Union[Base, DeclarativeMeta],
        *filters: Iterable,
        **values: dict,
    ) -> Union[int, Base]:
        '''
        Update the database.

        Usage examples::

            # merge user instance
            client.update(user)

            # update user.id to '10' and then merge the instance
            client.update(user, user.id='10')

            # Update all users names to 'John Doe' if their age is > 35
            client.update(User, User.age > 35, User.name='John Doe')

        :param model: Table or an instance of table row to update
        :param filters: Filtering options. applied only when updating the whole table (not a single instance).
         If there are no filters, update will be applied to the all rows of the Table. **BE CAREFUL!!!
        :param values: New values to set while updating the table. If ``model`` is a singe instance of a Table,
         values will be applied only to this instance, if ``model`` is a Table, values will be applied to all
         instances that are filtered out with ``filters``.
        :return: Number of updated instances or updated instance depending on type of the first parameter.
        '''
        if isinstance(model, DeclarativeMeta):  # model is table
            # check if keys of ``values`` are valid
            if not values:
                raise ValueError('**values must not be None or empty when model is a Table')
            for k, _ in values.items():
                if not hasattr(model, k):
                    raise ValueError(f'{model.name} has no attribute {k}')
            with self.session() as session:
                result = session.query(model)
                for filter_ in filters:
                    if filter_ is not None:
                        result = result.filter(filter_)
                result = result.update(values)
            return result
        else:  # model is instance of a table
            if values:
                for k, v in values.items():
                    if not hasattr(model, k):
                        raise ValueError(f'{type(model).name} has no attribute {k}')
                    setattr(model, k, v)
            with self.session() as session:
                merged = session.merge(model)
            return merged

    def delete(self, model: Base) -> None:
        '''
        Delete model from the database.

        :param model: Instance of a model to delete.
        :return: None
        '''
        with self.session() as session:
            session.delete(model)

    def __create_tables(self):
        Base.metadata.create_all(bind=self.__engine)

    def __create_engine(self) -> Engine:
        conn_str = f'sqlite+pysqlite:///{self.__storage_path}'
        engine = create_engine(conn_str, echo=False)
        return engine

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()