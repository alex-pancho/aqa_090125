from abc import ABC, abstractmethod
from variables import webdriver

# Абстрактний клас тварини
class Animal(ABC):

    def __init__(self, name:str):
        self.name = name.title()
    
    @abstractmethod
    def make_sound(self):
        pass


# Клас собаки, що успадковує абстрактний клас Animal
class Dog(Animal):

    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

class BaseUITest(ABC):
    def __init__(self, url):
        self.driver = webdriver.chrome()
        self.url = url

    def open_page(self):
        self.get = webdriver.get(self.url)

    @abstractmethod
    def test_run(self):
        """Кожен тест повинен мати свою власну реалізацію"""
        pass

    def close(self):
        pass

class LoginTest(BaseUITest):
    def __init__(self):
        super().__init__("https://example.com/login")

    def test_run(self):
        self.open_page()
        # Додати логіку тесту

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

class UserTest(BaseAPITest):
    def test_endpoint(self):
        data = {"username": "test_user", "password": "123456"}
        response = self.post("/login", data)
        assert response["status"] == "success"



if __name__ == "__main__":
    bingo = Dog("bingo")
    print(bingo.make_sound())
    print(bingo.name)
    cat = Cat("Whiskers")
    bird = Bird("Sparrow")

    # test = UserTest()
    # test.test_endpoint()