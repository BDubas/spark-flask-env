#!/bin/bash

cd shared/db
python3 schema.py
cd -

sudo ./build.sh

sudo docker-compose up
