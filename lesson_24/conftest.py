import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth
from logger import logger

@pytest.fixture(scope="function")
def get_regisered_user():
    email = "alex22222@gmail.com"
    password = "AA12aa!@"
    query_data = {
        "name": "name",
        "lastName": "lastname",
        "email": email,
        "password": password,
        "repeatPassword": password
    }
    s = requests.Session()
    r = requests.get(s, request_body=query_data)
    if r.status_code != 201:
        raise AttributeError(r.text)
    yield email, password
    requests.delete(s)


@pytest.fixture(scope="function", autouse=True)
def my_printable_fixture(request):
    print(f"Test {request.node.name}")
    yield
    print("Test end message")


@pytest.fixture(params=[1, 2, 3])
def my_fixture(request):
    param_value = request.param
    print(f"Setup with param value: {param_value}")
    return param_value * 2


# Параметризована фікстура
@pytest.fixture(params=[requests.get, requests.post])
def http_method(request):
    return request.param


@pytest.fixture(scope='class')
def prepare_database():
    print("Підготовка бази даних...")
    yield
    print("Очищення бази даних...")


@pytest.fixture(scope='class')
def prepare_config():
    print("Підготовка конфігурації...")
    yield
    print("Очищення конфігурації...")

# fixture for test cars IPI

BASE_URL = 'http://127.0.0.1:8080'
USERS = {"test_user": "test_pass"}

logger()

@pytest.fixture(scope='class')
def api_session():
    """Створює сесію з токеном доступу для API."""
    logging.info("User auth...")
    session = requests.Session()
    auth = HTTPBasicAuth('test_user', 'test_pass')
    response = session.post(f'{BASE_URL}/auth', auth=auth)
    assert response.status_code == 200
    token_data = response.json()
    assert 'access_token' in token_data
    access_token = token_data['access_token']
    session.headers.update({'Authorization': f'Bearer {access_token}'})
    logging.info(f"Token: {access_token[:20]}...")
    yield session
    session.close()
    logging.info("Session closed")
