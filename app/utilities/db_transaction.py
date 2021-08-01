# -*- coding: utf-8 -*-
from lib.db import PostgresDB, CursorPool

auth = {'host': 'localhost',
        'usr': 'postgres',
        'port': '5432',
        'pwd': 'cargamosShop',
        'db': 'Cargamos_Inventory'}

PostgresDB.initialize(auth)

class Transaction:

    def __init__(self) -> None:
        pass

    
    def pull_shops(self, query):
        with CursorPool(auth) as cursor:
            cursor.execute(query)
            columns = list(cursor.description)
            data = cursor.fetchall()
            results = [dict(row) for row in data]
        return results
    

    def pull_product(self, query):
        with CursorPool(auth) as cursor:
            cursor.execute(query)
            columns = list(cursor.description)
            data = cursor.fetchall()
            response = [dict(row) for row in data]
            print(response)


    def insert_product(self):
        pass


    def update_product(self):
        pass

    
    def get_shop(self):
        pass


    def insert_shop(self):
        pass


    def update_shop(self):
        pass



