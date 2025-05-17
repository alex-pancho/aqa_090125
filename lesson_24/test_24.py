import pytest
import requests


class TestClass:
    def test_1(self):
        assert 1 == 1 
    
    def test_2(self):
        assert True
    
    def test_3(self):
        assert True

    def test_4(self):
        assert True

def test_5():
    assert True


# Приклад використання фікстури у тесті
def test_using_fixture(my_fixture):
    print(f"Test with fixture value: {my_fixture}")
    assert my_fixture % 2 == 0


# Тестова функція
def test_http_methods(http_method):
    url = "https://httpbin.org/" 
    url = url + "/get" if http_method == requests.get else url + "/post"
    data = {"example": "data"}
    if http_method == requests.get:
        response = http_method(url, params=data)
    else:
        response = http_method(url, data=data)

    assert response.status_code == 200
    json_data = response.json()

    if http_method == requests.get:
        assert json_data["args"] == data
    else:
        assert json_data["form"] == data


@pytest.mark.usefixtures("prepare_database")
class TestClassWithDatabase:
    def test_method1(self):
        print("Тестування методу 1...")

    def test_method2(self):
        print("Тестування методу 2...")


@pytest.mark.usefixtures("prepare_config")
class TestClassWithConfig:
    def test_method3(self):
        print("Тестування методу 3...")

    def test_method4(self):
        print("Тестування методу 4...")


class TestClassWithMultipleFixtures:
    def test_method1(self):
        print("Тестування методу 5...")

    def test_method2(self):
        print("Тестування методу 6...")


def add(x, y):
    return x + y


@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (10, -5, 5)
])
def test_addition(x, y, expected):
    result = add(x, y)
    assert result == expected

# out = map(add, [1,1,1], [2,3,7])
# print(*out)


@pytest.fixture
def prepare_data(request):
    data = request.param * 2
    return data


# Параметризований тест з використанням фікстури та параметра indirect
@pytest.mark.parametrize("prepare_data", [1, 2, 3], indirect=True)
def test_example(prepare_data):
    print(prepare_data)
    assert prepare_data % 2 == 0

