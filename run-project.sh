#!/bin/bash

json-server --watch database.json &
python3 server.py