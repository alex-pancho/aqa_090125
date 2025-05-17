Абстрактні класи — це відмінний інструмент для тестувальників-автоматизаторів, оскільки вони дозволяють створювати загальні шаблони для тестів, які можна легко розширювати.  

Ось кілька цікавих прикладів використання абстрактних класів у Python для автоматизованого тестування:

---

### 1️⃣ **Базовий клас для UI тестів (Selenium)**
Цей клас задає загальні методи для взаємодії з веб-сторінками, а конкретні тести будуть наслідувати його.

```python
from abc import ABC, abstractmethod
from selenium import webdriver

class BaseUITest(ABC):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_page(self, url):
        self.driver.get(url)

    @abstractmethod
    def run_test(self):
        """Кожен тест повинен мати свою власну реалізацію"""
        pass

    def close(self):
        self.driver.quit()
```

### Використання:
```python
class LoginTest(BaseUITest):
    def run_test(self):
        self.open_page("https://example.com/login")
        # Додати логіку тесту

test = LoginTest()
test.run_test()
test.close()
```

---

### 2️⃣ **Базовий клас для API тестування (Requests)**
Такий клас спрощує роботу з API, задаючи стандартні методи для запитів.

```python
import requests
from abc import ABC, abstractmethod

class BaseAPITest(ABC):
    BASE_URL = "https://api.example.com"

    @abstractmethod
    def test_endpoint(self):
        """Кожен тест повинен реалізувати цей метод"""
        pass

    def get(self, endpoint):
        response = requests.get(self.BASE_URL + endpoint)
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(self.BASE_URL + endpoint, json=data)
        return response.json()
```

### Використання:
```python
class UserTest(BaseAPITest):
    def test_endpoint(self):
        data = {"username": "test_user", "password": "123456"}
        response = self.post("/login", data)
        assert response["status"] == "success"

test = UserTest()
test.test_endpoint()
```

---

### 3️⃣ **Базовий клас для тестування БД (SQLAlchemy)**
Корисний для інтеграційних тестів, що працюють з базами даних.

```python
from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class BaseDBTest(ABC):
    DB_URL = "sqlite:///:memory:"

    def __init__(self):
        self.engine = create_engine(self.DB_URL)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    @abstractmethod
    def run_test(self):
        """Тест повинен реалізувати цей метод"""
        pass
```

### Використання:
```python
class UserDBTest(BaseDBTest):
    def run_test(self):
        result = self.session.execute("SELECT 1")
        assert result.fetchone()[0] == 1

test = UserDBTest()
test.run_test()
```

---

### 🔹 **Абстрактний клас для роботи з датою та часом**
```python
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class BaseDateTimeProcessor(ABC):
    """Абстрактний клас для роботи з датою та часом."""

    def __init__(self):
        self.current_time = datetime.now()

    def get_current_time(self):
        """Повертає поточний час."""
        return self.current_time

    def add_days(self, days: int):
        """Додає певну кількість днів до поточної дати."""
        return self.current_time + timedelta(days=days)

    def subtract_days(self, days: int):
        """Віднімає певну кількість днів від поточної дати."""
        return self.current_time - timedelta(days=days)

    @abstractmethod
    def process_time(self):
        """Абстрактний метод, який має бути реалізований у підкласах."""
        pass
```

---

### 🔹 **Реалізація конкретного класу**
#### 1️⃣ Клас для форматування дати  
```python
class DateFormatter(BaseDateTimeProcessor):
    def process_time(self):
        """Форматує дату у вигляді рядка."""
        return self.get_current_time().strftime("%Y-%m-%d %H:%M:%S")

# Використання:
formatter = DateFormatter()
print(formatter.process_time())  # Наприклад: "2025-03-17 12:45:30"
```

#### 2️⃣ Клас для перевірки, чи вихідний день  
```python
class WeekendChecker(BaseDateTimeProcessor):
    def process_time(self):
        """Перевіряє, чи поточна дата є вихідним днем (субота або неділя)."""
        return self.get_current_time().weekday() in [5, 6]

# Використання:
checker = WeekendChecker()
print(checker.process_time())  # True або False залежно від дня тижня
```

#### 3️⃣ Клас для підрахунку різниці між датами  
```python
class DateDifferenceCalculator(BaseDateTimeProcessor):
    def process_time(self, other_date: datetime):
        """Обчислює різницю між поточною датою і переданою датою."""
        return abs((self.get_current_time() - other_date).days)

# Використання:
calculator = DateDifferenceCalculator()
date_in_past = datetime(2024, 1, 1)
print(calculator.process_time(date_in_past))  # Виведе, наприклад, 76 днів
```

---

Ці класи допомагають тестувальникам автоматизаторам швидко створювати нові тести, дотримуючись принципів **DRY (Don't Repeat Yourself)** і **SOLID (особливо Open/Closed Principle)**.
