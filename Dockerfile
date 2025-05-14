# Використовуємо офіційний образ Python версії 3.9
FROM python:3.9

# Створюємо робочу директорію
WORKDIR /app

# Копіюємо requirements.txt і встановлюємо залежності
COPY requirements.txt .
RUN pip install -r requirements.txt

# Встановлюємо Allure CLI
RUN pip install allure-pytest \
    && curl -o allure.tgz -L https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz \
    && tar -xzf allure.tgz \
    && mv allure-2.27.0 /opt/allure \
    && ln -s /opt/allure/bin/allure /usr/bin/allure \
    && rm allure.tgz

# Копіюємо весь проєкт у контейнер
COPY . .

# Не запускаємо тести автоматично — це зробить Jenkins
CMD ["sleep", "infinity"]
