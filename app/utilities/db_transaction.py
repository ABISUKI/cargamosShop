# -*- coding: utf-8 -*-
from psycopg2 import IntegrityError
from lib.db import PostgresDB, CursorPool
from etc import SETTINGS


PostgresDB.initialize(auth=SETTINGS["db"]["postgress_auth"])

class Transaction:

    def __init__(self) -> None:
        pass

    
    def pull(self, query):
        with CursorPool() as cursor:
            cursor.execute(query)
            columns = list(cursor.description)
            data = cursor.fetchall()
        return [dict(row) for row in data]
    
    def insert(self, query, values):
        try:
            with CursorPool() as cursor:
                cursor.execute(query, values)
                print("insertion succesfull")
            return True, "New data registered"
        
        except (IntegrityError, Exception) as e:
            if "duplicate key value violates" in str(e):
                return False, "Shop/warehouse already exist"
            return False, str(e)

    
    def update(self):
        pass


