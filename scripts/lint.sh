#!/bin/sh
set -e

echo "Running pylint .."
pylint web

if [ "$ENV" = "CI" ]
then
  echo "Running codecov .."
  codecov
fi
