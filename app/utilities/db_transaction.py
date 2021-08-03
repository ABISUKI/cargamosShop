# -*- coding: utf-8 -*-
from psycopg2 import IntegrityError
from lib.db import PostgresDB, CursorPool
from etc import SETTINGS
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass

PostgresDB.initialize(auth=SETTINGS["db"]["postgress_auth"])

@dataclass
class Transaction:

    def pull(self, query: str) -> List[Dict]:
        with CursorPool() as cursor:
            cursor.execute(query)
            columns = list(cursor.description)
            data = cursor.fetchall()
        return [dict(row) for row in data]
    

    def insert(self, query:str, values: list) -> Tuple[bool, str]:
        try:
            with CursorPool() as cursor:
                cursor.execute(query, values)
                print("insertion succesfull")
            return True, "New data registered"
        
        except (IntegrityError, Exception) as e:
            if "duplicate key value violates" in str(e):
                return False, "Shop/warehouse already exist"
            return False, str(e)


    def update(self, query: str) -> Tuple[bool, Any]:
        try:
            with CursorPool() as cursor:
                cursor.execute(query)
            return True, None
        except Exception  as e:
            return False, str(e)