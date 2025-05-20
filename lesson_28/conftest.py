import pytest
import random
from selenium import webdriver
from api_client import ApiClient
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.garage_page import GaragePage

URL = "https://guest:welcome2qauto@qauto.forstudy.space"

@pytest.fixture(scope="module")
def driver():
    """Ініціалізація браузера."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()

@pytest.fixture
def api_client():
    """API-клієнт для роботи з бекендом."""
    return ApiClient()

@pytest.fixture
def home_page(driver):
    """Фікстура для сторінки Home."""
    return HomePage(driver)

@pytest.fixture
def registration_page(driver):
    """Фікстура для модального вікна реєстрації."""
    return RegistrationPage(driver)

@pytest.fixture
def garage_page(driver):
    """Фікстура для сторінки Garage."""
    return GaragePage(driver)

@pytest.fixture
def fill_registration_form(registration_page, api_client):
    """Фікстура реєстрації користувача."""
    created_user = {}

    def _fill():
        unique_email = f"test{random.randint(1000, 9999)}@gmail.com"
        registration_page.open_registration_modal()
        registration_page.fill_form(
            name="Test",
            last_name="Tester",
            email=unique_email,
            password="Test1234"
        )
        registration_page.submit_form()
        created_user["email"] = unique_email
        created_user["password"] = "Test1234"
        return unique_email
    
    yield _fill

    # Видалення створеного користувача після тесту
    if created_user:
        try:
            api_client.login(created_user["email"], created_user["password"])
            api_client.delete_user()
        except Exception as e:
            print("Помилка при видаленні користувача:", e)
