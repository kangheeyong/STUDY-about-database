FROM python:3.8

RUN apt-get update
RUN pip install --upgrade pip

RUN pip install mongoengine
RUN pip install mongo-types
RUN pip install psycopg2
RUN pip install mypy

RUN mkdir -p /example

WORKDIR /example
