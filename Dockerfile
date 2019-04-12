FROM python:3.7-alpine

RUN apk update && apk add --virtual build-dependencies build-base gcc

COPY requirements/* /tmp/

RUN pip install -r /tmp/dev.txt

RUN rm /tmp/*.txt

WORKDIR /opt
