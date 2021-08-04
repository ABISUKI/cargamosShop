#!/bin/bash

sudo apt-get install python3-pip
sudo apt-get install python-psycopg2
sudp apt-get install python-pytest
pip install virtualenv
sudo pip3 install virtualenv
virtualenv env-shop -p python3
source env-shop/bin/activate
pip3 install -r requirements.txt


