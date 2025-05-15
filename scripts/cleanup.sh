#!/bin/bash
set -e

echo "🧹 Останавливаем и удаляем контейнеры Docker Compose..."
docker-compose -p test down -v --remove-orphans || true

echo "🧹 Удаляем все контейнеры с именами, начинающимися на jenkins_test_..."
docker ps -a --filter "name=pytest_app_" --format "{{.ID}}" | while read id; do
  echo "Удаляем контейнер $id"
  docker rm -f "$id" || true
done

echo "⚠️ Проверяем занятость порта 5436..."

pid=$(lsof -ti tcp:5438)
if [ -n "$pid" ]; then
  echo "🔌 Порт 5438 занят процессом PID $pid. Убиваем процесс..."
  kill -9 $pid || true
else
  echo "✅ Порт 5436 свободен"
fi

echo "✅ Очистка завершена"
