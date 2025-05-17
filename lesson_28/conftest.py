import pytest
import random

from get_browser import firefox, chrome
from pages.home_page import HomePage
from pages.garage_page import GaragePage
from pages.registration_page import RegistrationPage
from api_client import ApiClient



URL = "https://guest:welcome2qauto@qauto.forstudy.space"

@pytest.fixture(scope="module")
def driver():
    _driver = firefox()
    _driver.maximize_window()
    _driver.get(URL)
    yield _driver
    _driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def garage_page(driver):
    return GaragePage(driver)

@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)

@pytest.fixture
def fill_registration_form(registration_page):
    created_user = {}

    def _fill():
        registration_page.item("sign_up_button").click()
        registration_page.item("name_field").wait_until_not_visible()
        registration_page.item("name_field").send_keys("Test")
        registration_page.item("last_name_field").send_keys("Tester")
        unique_email = f"test{random.randint(1000, 9999)}@gmail.com"
        registration_page.item("email_field").send_keys(unique_email)
        registration_page.item("password_field").send_keys("Test1234")
        registration_page.item("re_enter_password_field").send_keys("Test1234")
        registration_page.item("register_button").click()
        created_user["email"] = unique_email
        created_user["password"] = "Test1234"
        return unique_email
    
    yield _fill

    if created_user:
        api = ApiClient()
        try:
            api.login(created_user["email"], created_user["password"])
            api.delete_user()
        except Exception as e:
            print("Помилка при видаленні користувача:", e)

@pytest.fixture
def check_redirect_to_garage(registration_page):
    def _check():
        return registration_page.item("garage_heading").get_text()
    return _check
