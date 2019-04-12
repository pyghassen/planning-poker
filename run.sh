#!/usr/bin/env bash

echo "Starting the Planning poker server"
set -e
docker-compose up --build -d web
