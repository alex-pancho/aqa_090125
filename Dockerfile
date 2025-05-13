# Використовуємо офіційний образ Python версії 3.9
FROM python:3.9
COPY requirements.txt /app/requirements.txt
# Встановлюємо залежності для тестування
RUN pip install -r app/requirements.txt
# -r requirements.txt
# Установка allure-pytest и скачивание CLI
RUN pip install allure-pytest \
    && curl -o allure.tgz -L https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz \
    && tar -xzf allure.tgz \
    && mv allure-2.27.0 /opt/allure \
    && ln -s /opt/allure/bin/allure /usr/bin/allure
# Копіюємо файли з локальної директорії в контейнер
COPY . /app
# Задаємо робочу директорію контейнера
WORKDIR /app
# Виконуємо команду для запуску тестів під час створення контейнера
CMD ["python", "-m", "pytest", "-v", "/app/lesson_29", "--alluredir=/app/allure-results"]
