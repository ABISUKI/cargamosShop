import operator
import time
from flask import json, jsonify
from .db_transaction import Transaction
from etc import SETTINGS


class Sku:

    @classmethod
    def type_validation(cls, payload):
        if not payload["class"].upper() in SETTINGS["definition_type"]["product_class"]:
            return False, "product class not exists"
        if not payload["type"].upper()  in SETTINGS["definition_type"]["product_tags"].keys():
            return False, "product type not exists"
        if not payload["brand"].upper()  in SETTINGS["definition_type"]["brand_tags"].keys():
            return False, "Brand not registered, pleas make a request to add new brand"
        return True, None
        


    @classmethod
    def generate(cls, payload):
        validation = Sku.type_validation(payload)
        if validation[0]:
            sku = payload["class"] + SETTINGS["definition_type"]["product_tags"][payload["type"].upper()] + \
                payload["model"] + SETTINGS["definition_type"]["brand_tags"][payload["brand"].upper()]
            sku = sku.upper().replace(" ","")
            return True, sku
        else:
            return validation


class ResquestHanlder(Transaction):
    def __init__(self) -> None:
        Transaction.__init__(self)
        

    def pull_shops(self) -> json:
        query = SETTINGS["queries"]["get_shops"]
        results = self.pull(query)
        return jsonify({"Response": results})


    def pull_shop(self, name) -> json:
        query = SETTINGS["queries"]["get_shop"]
        query = query.format(name)
        results = self.pull(query)
        return jsonify({"Response": results})
    

    def insert_shop(self, payload) -> json:
        columns = []
        values = []
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
            return jsonify({"Response":"New shop registered"})
        return jsonify({"Response": results[1]})
    

    def pull_product(self, sku) -> json:
        query = SETTINGS["queries"]["get_product"]
        query_warehosue = SETTINGS["queries"]["get_shop_warehosue"]
        query = query = query.format(sku)
        results = self.pull(query)
        if len(results) > 0:
            print(results[0])
            query_warehosue = query_warehosue.format(results[0]["warehouse"], results[0]["shop"])
            print(query_warehosue)
            results2 = self.pull(query_warehosue)
            return jsonify({"Response": {"stock": len(results),
                                        "location": results2},
                                        "first result": results[0]})
        else:
            return jsonify({"Response": "SKU not exist"})

        

    def insert_product(self, payload):
        columns = []
        values = []
        query = SETTINGS["queries"]["add_product"]
        
        sku_result = Sku.generate(payload)
        if not sku_result[0]:
            return jsonify({"Response": sku_result[1]})
        payload.update({"sku": sku_result[1]})
        payload_sorted = sorted(payload.items(), key=operator.itemgetter(0))
        for row in payload_sorted:
            columns.append(row[0])
            values.append(row[1])
        columns = str(columns).replace("'","")\
                              .replace("[", "")\
                              .replace("]", "")
        query = query.format(columns)
        print(query)
        print(values)
        results = self.insert(query, values)
        if results[0]:
            return jsonify({"Response": f"New product registered, SKU: {sku_result[1]}"})
        return jsonify({"Response": results[1]})

        