"""
    Endpoints testing.
"""

import os
import requests

HOST = os.environ["FLASK_HOST"]
PORT = os.environ["FLASK_PORT"]

def test_get_shop():
    response = requests.get(f"http://{HOST}:{PORT}/product/inventory/ELPHNP30LITEHWI")
    data = response.json()
    assert data["error"] == None
    assert response.status_code == 200

def test_get_shops():
    response = requests.get(f"http://{HOST}:{PORT}/shop/all")
    data = response.json()
    assert data["error"] == None
    assert response.status_code == 200