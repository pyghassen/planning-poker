#!/bin/sh
set -e

echo "Starting the Planning poker server"
python web/manage.py runserver 0.0.0.0:8000
