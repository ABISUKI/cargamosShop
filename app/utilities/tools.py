from datetime import time
from flask import jsonify
import re
from .db_transaction import Transaction
from etc import SETTINGS
import time



class GenerateSku:
    def __init__(self) -> None:
        pass


class ResquestHanlder(Transaction):
    def __init__(self) -> None:
        Transaction.__init__(self)
        

    def pull_shops_handler(self):
        query = SETTINGS["queries"]["get_shops"]
        results = self.pull_shops(query)
        return jsonify({"Response": results})

    def pull_shop_handler(self, name):
        query = SETTINGS["queries"]["get_shop"]
        query = query.format(name)
        results = self.pull_shops(query)
        print(results)
        time.sleep(5)
        return jsonify({"Response": results})