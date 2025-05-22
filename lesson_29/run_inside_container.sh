#!/bin/sh

python wait_for_postgres.py

pytest tests/test_db.py --alluredir=allure-results

zip -r results.zip allure-results

curl -X POST http://host.docker.internal:5050/allure-docker-service/send-results?project_id=lesson-30 \
     -H "Content-Type: multipart/form-data" \
     -F results=@results.zip