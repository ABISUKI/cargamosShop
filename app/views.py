# -*- coding: utf-8 -*-f
from flask import Flask
from flask_restx import Api, Resource

app  = Flask(__name__)
api = Api(app)


@api.route("/hello")
class HelloWord(Resource):
    def get(self):
        return {'hello': 'world'}
