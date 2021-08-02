# -*- coding: utf-8 -*-f
import os
print(os.environ["POSTGRES_PWD"])
from .services.api_setup import *
from .utilities.tools import ResquestHanlder

request_handler = ResquestHanlder()

@api.route("/shop/")
class Shop(Resource):
    @api.expect(model_shop, validate=True)
    def post(self):
        json_response = request.get_json(silent=True, cache=False)
        return request_handler.insert_shop(json_response)


@api.route("/shop/<name>")
class Shop(Resource):
    @api.doc(params={'name': 'The shop name'})
    def get(self, name):
        if name == "all":
            return request_handler.pull_shops()
        return request_handler.pull_shop(name)


@api.route("/product/<sku>")
class Product(Resource):
    @api.doc(params={'sku': 'SKU Code'})
    def get(self, sku):
        return request_handler.pull_product(sku)


@api.route("/product/")
class Product(Resource):
    @api.expect(model_product, validate=True)
    def post(self):
        json_response = request.get_json(silent=True, cache=False)
        return request_handler.insert_product(json_response)