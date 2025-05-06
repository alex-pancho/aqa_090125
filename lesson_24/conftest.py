import pytest
import requests
from requests.auth import HTTPBasicAuth

# Логуюча фікстура — показує назву тесту на старт/завершення
@pytest.fixture(scope="function", autouse=True)
def my_printable_fixture(request):
    print(f"🔹 Start test: {request.node.name}")
    yield
    print("🔻 End of test")

# Параметризована фікстура — приклад із числами
@pytest.fixture(params=[1, 2, 3])
def my_fixture(request):
    param_value = request.param
    print(f"Setup with param value: {param_value}")
    return param_value * 2

# Параметризована фікстура для HTTP методів
@pytest.fixture(params=[requests.get, requests.post])
def http_method(request):
    return request.param

# Підготовка конфігурації
@pytest.fixture(scope='class')
def prepare_config():
    print("🔧 Підготовка конфігурації...")
    yield
    print("🧹 Очищення конфігурації...")

# Підготовка бази даних
@pytest.fixture(scope='class')
def prepare_database():
    print("🗃️ Підготовка бази даних...")
    yield
    print("🧼 Очищення бази даних...")

# Додаткова фікстура: отримання токену (може бути використано окремо)
@pytest.fixture(scope="function")
def auth_headers():
    base_url = "http://127.0.0.1:8080"
    auth = HTTPBasicAuth("test_user", "test_pass")
    response = requests.post(f"{base_url}/auth", auth=auth)
    assert response.status_code == 200
    token = response.json().get("access_token")
    assert token, "Токен не отримано"
    return {"Authorization": f"Bearer {token}"}
