# -*- coding: utf-8 -*-
import os

from etc import SETTINGS
import os
import psycopg2
from psycopg2 import pool
from psycopg2.extensions import POLL_ERROR
from psycopg2.extras import DictCursor
from psycopg2.pool import SimpleConnectionPool


class PostgresDB:
    __pool = None

    @classmethod
    def initialize(cls, auth: dict) -> None:
        cls.__pool = SimpleConnectionPool(minconn=2,
                                          maxconn=5,
                                          cursor_factory=DictCursor,
                                          database=auth["db"],
                                          user=os.environ[auth["usr"]],
                                          password=os.environ[auth["pwd"]],
                                          host=auth["host"],
                                          port=auth["port"])
    

    @classmethod
    def get_connection(cls) -> object:
        return cls.__pool.getconn()


    @classmethod
    def return_connection(cls, connection: object) -> None:
        PostgresDB.__pool.putconn(connection)


    @classmethod
    def close_all_connections(cls) -> None:
        PostgresDB.__pool.closeall()


class CursorPool():
    """Get a cursor from a connection from pool of connections."""

    def __init__(self):
        self.connection = None
        self._cursor = None


    def __enter__(self) -> object:
        # get a connection from the pool
        self.connection = PostgresDB.get_connection()
        self._cursor = self.connection.cursor()
        return self._cursor
    

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        # Rollback if not everything is good
        if exc_val is not None:
            self.connection.rollback()
        else:
            self._cursor.close()
            # commit the connection otherwise nothing is gonna write
            self.connection.commit()
        # put it back to pool
        PostgresDB.return_connection(self.connection)
