# -*- coding: utf-8 -*-
import app
from lib.dep import*
from app.views import app
print("Hello Starting applicationnn")



host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(host_ip)
if __name__ == '__main__':
    app.run(host=host_ip, debug=True)