# -*- coding: utf-8 -*-
import app
from lib.dep import*
from app.views import app

HOST = os.environ["FLASK_HOST"]

if __name__ == '__main__':
    app.run(host=HOST, port=8080, debug=True)