# -*- coding: utf-8 -*-

import json
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields, namespace


app  = Flask(__name__)
app.config['RESTX_VALIDATE'] = True
api = Api(app, title="DEMO", description="description", default_label='Shop Invenotry', default="CargamosShop")


model_shop = api.model('Shop', {
                       'name': fields.String(example="cargamosShop", required=True),
                       'warehouse': fields.String(example="A1", required=True),
                       'address': fields.String(example="Av 12 #1854", required=True),
                       'city': fields.String(example="Guadalajara", required=True),
                       'country': fields.String(example="Mexico", required=True),
                       'state': fields.String(example="Jalisco", required=True),
                       'phone': fields.String(example="+5213325653908", required=True),
                       'opening_time': fields.String(example="08:30", required=True, description="Format 24h Opening hours"),
                       'closing_time': fields.String(example="22:00", required=True, description="Format 24h Closgin hours"),
                       })


model_product = api.model('Product', {
                          'type': fields.String(example="Phone", required=True, description="Just existing types"),
                          'model': fields.String(example="P30 Lite", required=True),
                          'brand': fields.String(example="Huawei", required=True),
                          'color': fields.String(example="black", required=True),
                          'status': fields.String(example="true", required=True),
                          'class': fields.String(example="EL", required=True, description="EL = Electronic etc.."),
                          'warehouse': fields.String(example="A1", required=True, description="To assing to an existing warehouse/store"),
                          'shop': fields.String(example="cargamosShop", required=True),
                          'extra': fields.String(example="memmory 4rm-128", required=True)})



model_product_update = api.model('ProductUpdate', {
                          'type': fields.String(example="Phone", required=False, description="Just existing types"),
                          'model': fields.String(example="P30 Lite", required=False),
                          'brand': fields.String(example="Huawei", required=False),
                          'color': fields.String(example="black", required=False),
                          'status': fields.String(example="true", required=False),
                          'class': fields.String(example="EL", required=False, description="EL = Electronic etc.."),
                          'warehouse': fields.String(example="A1", required=False, description="To assing to an existing warehouse/store"),
                          'shop': fields.String(example="cargamosShop", required=False),
                          'extra': fields.String(example="memmory 4rm-128", required=False)})

