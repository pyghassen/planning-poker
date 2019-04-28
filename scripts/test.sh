#!/bin/sh
set -e

echo "Running tests .."
coverage run --source='web' web/manage.py test web
coverage report
