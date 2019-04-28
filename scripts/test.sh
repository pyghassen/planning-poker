#!/bin/sh
set -e

# python -m pytest -vv -s -x --cov=app --cov-branch --cov-report term-missing  --no-cov-on-fail tests/
python web/manage.py test web
