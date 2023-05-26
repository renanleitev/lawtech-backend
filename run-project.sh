#!/bin/bash

path=$(pwd)/openssl.cnf

export OPENSSL_CONF=$path;
json-server --watch database.json &
python3 server.py
