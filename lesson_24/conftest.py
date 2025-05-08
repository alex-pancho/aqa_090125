import pytest
import requests

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
