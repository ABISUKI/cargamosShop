# -*- coding: utf-8 -*-f
from flask import Flask
from flask_restx import Api, Resource

app  = Flask(__name__)
api = Api(app)


@api.route("/shops")
class Shops(Resource):
    def get(self):
        return {'get': 'method'}

@api.route("/shop")
class Shop(Resource):
    def get(self):
        return {'get': 'method'}
    
    def post(self):
        return {'Post': 'method'}



@api.route("/products")
class Products(Resource):
    def get(self):
        return {'get': 'method'}

@api.route("/product")
class Product(Resource):
    def get(self):
        return {'get': 'method'}
    
    def post(self):
        return {'Post': 'method'}