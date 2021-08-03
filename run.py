# -*- coding: utf-8 -*-
import app
from lib.dep import*
from app.views import app

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(host_name)
HOST = os.environ["FLASK_HOST"]

if __name__ == '__main__':
    app.run(host=HOST, port=8080, debug=True)