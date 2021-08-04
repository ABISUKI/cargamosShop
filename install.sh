#!/bin/bash

echo "Staring process to install dependencies on linux(ubuntu) environment"
echo Installing  dependences and creating virtualenviromente
./environment.sh

echo Installing DB postgres, generating tables and first insertion required
./dbstart.sh

echo "Exporting temporal variables, please change it manually in source environment/bin/activate"

source env-shop/bin/activate
export POSTGRES_USER=postgres
export POSTGRES_PWD=postgres
export FLASK_HOST=0.0.0.0
export FLASK_PORT=8080
echo "Process finished"
