#!/bin/sh
set -e

if [ "$ENV" = "CI" ]
then
  echo "Running codecov .."
  codecov
fi

echo "Running pylint .."
pylint web
