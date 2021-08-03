import calendar
import operator
import re
import time
import pandas as pd
from datetime import datetime
from threading import Timer
from flask import json, jsonify, make_response
from werkzeug.wrappers import response
from .db_transaction import Transaction
from etc import SETTINGS
from typing import List, Tuple, Any


class Responses:

    @classmethod
    def success_response(cls, data) -> json:
        return make_response(jsonify({"Response": data, "error" : None}), 200)
    
    @classmethod
    def fail_response(cls, error) -> json:
        return make_response(jsonify({"Response": None, "error" : error}), 400)
    
    @classmethod
    def server_error_response(cls, error) -> json:
        return make_response(jsonify({"Response": None, "error" : error}), 500)


class Sku:

    @classmethod
    def type_validation(cls, payload: dict) -> Tuple[bool, Any]:
        if not payload["class"].upper() in SETTINGS["definition_type"]["product_class"]:
            return False, "product class not exists"
        if not payload["type"].upper()  in SETTINGS["definition_type"]["product_tags"].keys():
            return False, "product type not exists"
        if not payload["brand"].upper()  in SETTINGS["definition_type"]["brand_tags"].keys():
            return False, "Brand not registered, pleas make a request to add new brand"
        return True, None
        

    @classmethod
    def generate(cls, payload: dict) -> Tuple[bool, Any]:
        validation = Sku.type_validation(payload)
        if validation[0]:
            sku = payload["class"] + SETTINGS["definition_type"]["product_tags"][payload["type"].upper()] + \
                payload["model"] + SETTINGS["definition_type"]["brand_tags"][payload["brand"].upper()]
            sku = sku.upper().replace(" ","")
            return True, sku
        else:
            return validation
    

    @classmethod
    def generate_code_time(cls, sku) -> str:
        time_stamp = calendar.timegm(datetime.utcnow().timetuple())
        return str(time_stamp) + sku


class ResquestHanlder(Transaction):

    def __init__(self):
        Transaction.__init__(self)
        self.shop_warehouse = self.pull_shop_warehouse()


    def stock_product_to_shop(self, data_product: list) -> list:
        stock = []
        df_product = pd.DataFrame(data_product)
        for shop in self.shops:
            concurrence = df_product[df_product["shop"].str.contains(shop)]
            print(len(concurrence))
            if len(concurrence) > 0:
                stock.append({shop:len(concurrence)})
        return stock
                
    
    def pull_shop_warehouse(self) -> List[dict]:
        query = SETTINGS["queries"]["get_name_shops"]
        results = self.pull(query)
        names = [row["name"]for row in results[1]]
        self.shops = names = set(names)
        return results[1]


    def pull_shops(self) -> json:
        query = SETTINGS["queries"]["get_shops"]
        results = self.pull(query)
        if results[0]:
            return Responses.success_response(results[1])
        return Responses.server_error_response(results[1])


    def pull_shop(self, name: str) -> json:
        query = SETTINGS["queries"]["get_shop"]
        query = query.format(name)
        results = self.pull(query)
        if results[0]:
            return Responses.success_response(results[1])
        return Responses.server_error_response(results[1])
    

    def insert_shop(self, payload: dict) -> json:
        columns = []
        values = []

        for key in self.shop_warehouse:
            if key["name"] ==  payload["name"] and key["warehouse"] ==  payload["warehouse"]:
                return jsonify({"Response":"Shop/warehouse already exist"})

        query = SETTINGS["queries"]["add_shop"]
        schedule = payload["opening_time"] + "am - " + \
        payload["closing_time"] + "pm"
        payload.update({"schedule": schedule})
        del payload["closing_time"]
        del payload["opening_time"]
        payload_sorted = sorted(payload.items(), key=operator.itemgetter(0))
        for row in payload_sorted:
            columns.append(row[0])
            values.append(row[1])

        columns = str(columns).replace("'","")\
                              .replace("[", "")\
                              .replace("]", "")
        query = query.format(columns)
        
        results = self.insert(query, values)
        if results[0]:
            self.shop_warehouse.append({"name": payload["name"], "warehouse":payload["warehouse"]})
            return Responses.success_response("New shop registered")
        return Responses.server_error_response(results[1])
    

    def pull_product(self, sku: str) -> json:
        query = SETTINGS["queries"]["get_product"]
        query = query.format(sku)
        results = self.pull(query)
        if results[0]:
            if len(results[1]):
                stock = self.stock_product_to_shop(results[1])
                return Responses.success_response({"Full stock": len(results[1]),
                                                    "Stock by Shop": stock,
                                                    "Product":results[1]})
            else:
                return Responses.success_response("SKU not exist")
        else:
            return Responses.server_error_response(results[1])


    def insert_product(self, payload: str) -> json:
        columns = []
        values = []
        query = SETTINGS["queries"]["add_product"]

        sku_result = Sku.generate(payload)
        if not sku_result[0]:
            return jsonify({"Response": sku_result[1]})
        payload.update({"sku": sku_result[1]})
        code_time = Sku.generate_code_time(sku_result[1])
        payload.update({"idTime":code_time})
        payload_sorted = sorted(payload.items(), key=operator.itemgetter(0))
        for row in payload_sorted:
            columns.append(row[0])
            values.append(row[1])
        columns = str(columns).replace("'","")\
                              .replace("[", "")\
                              .replace("]", "")
        query = query.format(columns)
        results = self.insert(query, values)
        if results[0]:
            response = f"New product registered, SKU: {sku_result[1]}, Code Time: {code_time}"
            return Responses.success_response(response)
        return Responses.success_response(results[0])

    
    def update_product(self, code_time: str, payload: str) -> json:
        columns = []
        values = []
        str_set = ""
        if not code_time:
            return jsonify({"Error": "pleases fill SKU to folloging up"})
        query = SETTINGS["queries"]["update_product"]
        payload_sorted = sorted(payload.items(), key=operator.itemgetter(0))
        for row in payload_sorted:
            str_set = str_set + " " + row[0] + f"='{row[1]}'" + ","
        query = query.format(str_set[:-1], code_time)
        results = self.update(query)
        if results[0]:
            if results[1] > 0:
                return Responses.success_response("Product Updated")
            else:
                return Responses.fail_response("No data updated-Product doesn't  exist")
        return Responses.server_error_response(results[1])
