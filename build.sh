#!/usr/bin/env bash
python dockerfile_generator.py
docker-compose build
docker-compose down
docker-compose up -d
