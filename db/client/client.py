from contextlib import contextmanager
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, scoped_session

from budget.common.types import SqliteEndpointOutput, SqliteEndpointInput, Table
from budget.models import Base


class DbClient:
    '''
    Endpoint for SQLite database
    '''

    def __init__(self, storage_path: str):
        '''
        :param str storage_path: path to the storage file.db
        '''
        self._storage_path = storage_path
        self._engine = self._create_engine()
        session_factory = sessionmaker(bind=self._engine, expire_on_commit=False)
        self.session = scoped_session(session_factory)
        self._create_tables()

    def insert(self, table: Table, data: SqliteEndpointInput) -> SqliteEndpointOutput:
        '''
        insert a new model in the database.

        :param table: Table to use
        :type table: Base
        :param data: New model to insert
        :type data: Model
        :return: values of inserted model
        :rtype: SqliteEndpointOutput
        '''
        with self.session_scope() as session:
            session.add(data)
        return data

    def get(self, *entities, filters=(), limit=None, **kwargs) -> List[SqliteEndpointOutput]:
        with self.session_scope() as session:
            q = session.query(entities)
        for filter_arg in filters:
            q = q.filter(filter_arg)
        if limit:
            if limit > 1:
                return q.all()
            elif limit == 1:
                return q.first()
        return q.all()

    def update(self, table: Table, data: SqliteEndpointInput) -> SqliteEndpointOutput:
        with self.session_scope() as session:
            merged = session.merge(data)
        return merged

    def delete(self, table: Table, data: SqliteEndpointInput) -> None:
        with self.session_scope() as session:
            session.delete(data)

    def _create_tables(self):
        Base.metadata.create_all(bind=self._engine)

    def _create_engine(self) -> Engine:
        conn_str = 'sqlite+pysqlite:///%s' % self._storage_path
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