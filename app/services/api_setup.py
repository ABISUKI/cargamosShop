# -*- coding: utf-8 -*-

import json
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields, namespace


app  = Flask(__name__)
app.config['RESTX_VALIDATE'] = True
api = Api(app, title="DEMO", description="description", default_label='Shop Invenotry', default="CargamosShop")


model_shop = api.model('Shop', {
                       'name': fields.String(example="CragamosShop", required=True),
                       'warehouse': fields.String(example="A1", required=True),
                       'address': fields.String(example="Av 12 #1854", required=True),
                       'city': fields.String(example="Guadalajara", required=True),
                       'country': fields.String(example="Mexico", required=True),
                       'state': fields.String(example="Jalisco", required=True),
                       'phone': fields.String(example="+5213325653908", required=True),
                       'opening_time': fields.String(example="08:30", required=True, description="Format 24h Opening hours"),
                       'closing_time': fields.String(example="22:00", required=True, description="Format 24h Closgin hours"),
                       'not_working_days': fields.List(fields.String(example="monday"), required=True)})


model_product = api.model('Product', {
                          'type': fields.String(example="EL", required=True, description="EL = Electronic etc.."),
                          'model': fields.String(example="P30 Lite", required=True),
                          'brand': fields.String(example="Huawei", required=True),
                          'color': fields.String(example="black", required=True),
                          'class': fields.String(example="Samrt Phone", required=True),
                          'warehouse': fields.String(example="A1", required=True, description="To assing to an existing warehouse/store"),
                          'ram_memmory': fields.String(example="4", required=True),
                          'int_memmory': fields.String(example="168", required=True)})

#'status': fields.boolean(example="Guadalajara", required=False),