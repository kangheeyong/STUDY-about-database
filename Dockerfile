FROM python:3.8

RUN apt-get update
RUN pip install --upgrade pip

RUN pip install mongoengine
RUN pip install graphene
RUN pip install graphene-mongo
RUN pip install mongo-types
RUN pip install fastapi
RUN pip install uvicorn[standard]
RUN pip install psycopg2
RUN pip install mypy

RUN mkdir -p /example

WORKDIR /example
