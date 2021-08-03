# -*- coding: utf-8 -*-f
import os
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


@api.route("/product/inventory/<sku>")
class ProductInvenotry(Resource):
    @api.doc(params={'sku': 'SKU Code'})
    def get(self, sku):
        return request_handler.pull_product(sku)


@api.route("/product/")
class Product(Resource):
    @api.expect(model_product, validate=True)
    def post(self):
        json_response = request.get_json(silent=True, cache=False)
        return request_handler.insert_product(json_response)

  
    @api.doc(params={'codeTime': 'Code time ID'}, body=model_product_update)
    def put(self):
        code_time = request.args.get("codeTime")
        json_response = request.get_json(silent=True, cache=False)
        return request_handler.update_product(code_time, json_response)