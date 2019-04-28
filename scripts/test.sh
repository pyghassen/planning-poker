#!/bin/sh
set -e

echo "Running tests .."
python web/manage.py test web
