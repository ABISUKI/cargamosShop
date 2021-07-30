# -*- coding: utf-8 -*-f

from .services.api_setup import *

@api.route("/shops")
class Shops(Resource):
    
    def get(self):
        return {'get': 'method'}


@api.route("/shop")
class Shop(Resource):
    def get(self):
        return {'get': 'method'}
    

    @api.expect(model_shop, validate=True)
    def post(self):
        maybe_json = request.get_json(silent=True, cache=False)
        print(maybe_json)
        print(type(maybe_json))
        return jsonify(maybe_json)



@api.route("/products")
class Products(Resource):
    def get(self):
        return {'get': 'method'}


@api.route("/product")
class Product(Resource):
    def get(self):
        return {'get': 'method'}
    

    @api.expect(model_product, validate=True)
    def post(self):
        return {'Post': 'method'}