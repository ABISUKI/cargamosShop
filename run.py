# -*- coding: utf-8 -*-
import app
from lib.dep import*
from app.views import app

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)