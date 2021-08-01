# -*- coding: utf-8 -*-f

from .services.api_setup import *
from .utilities.tools import ResquestHanlder

request_handler = ResquestHanlder()

@api.route("/shop/")
class Shop(Resource):
    @api.expect(model_shop, validate=True)
    def post(self):
        maybe_json = request.get_json(silent=True, cache=False)
        print(maybe_json)
        print(type(maybe_json))
        return jsonify(maybe_json)

@api.route("/shop/<name>")
class Shop(Resource):
    @api.doc(params={'name': 'The shop name'})
    def get(self, name):
        if name == "all":
            return request_handler.pull_shops_handler()
        return request_handler.pull_shop_handler(name)


@api.route("/product")
class Product(Resource):
    def get(self):
        return {'get': 'method'}
    

    @api.expect(model_product, validate=True)
    def post(self):
        return {'Post': 'method'}