# Використовуємо офіційний образ Python версії 3.9
FROM python:3.9
COPY requirements.txt /app/requirements.txt
# Встановлюємо залежності для тестування
RUN pip install -r app/requirements.txt
# -r requirements.txt
# Копіюємо файли з локальної директорії в контейнер
COPY . /app
# Задаємо робочу директорію контейнера
WORKDIR /app
# Виконуємо команду для запуску тестів під час створення контейнера
CMD ["python", "-m", "pytest", "-v", "/app/lesson_29"]
