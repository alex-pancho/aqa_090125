#!/bin/sh
set -e

echo "▶️ Waiting for DB..."
python wait_for_postgres.py

echo "▶️ Waiting for Allure Viewer..."
for i in $(seq 1 30); do
  if curl --silent http://allure-viewer:5050/allure-docker-service/status | grep -q 'up'; then
    echo "✅ Allure Viewer is ready!"
    break
  fi
  echo "⏳ Waiting for Allure Viewer..."
  sleep 1
done

echo "▶️ Running tests..."
pytest tests/test_db.py --alluredir=allure-results

echo "▶️ Zipping results..."
apt-get update && apt-get install -y zip
zip -r results.zip allure-results

echo "▶️ Sending results to Allure..."
curl -X POST "http://allure-viewer:5050/allure-docker-service/send-results?project_id=lesson-30" \
     -H "Content-Type: multipart/form-data" \
     -F results=@results.zip