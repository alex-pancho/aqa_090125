import pytest
from requests.auth import HTTPBasicAuth

from lesson_28.get_browser import chrome
from selenium.webdriver import Chrome

from lesson_28.pages.home_page import HomePage
from lesson_28.pages.garage_page import GaragePage
from lesson_28.pages.homework_garage_page import HillelGaragePage
from lesson_28.pages.homework_home_page import HillelHomePage

URL = "https://guest:welcome2qauto@qauto.forstudy.space"
HOME_URL = "https://guest:welcome2qauto@qauto2.forstudy.space"
GARAGE_URL = "https://guest:welcome2qauto@qauto2.forstudy.space/panel/garage"

@pytest.fixture(scope="module")
def driver():
    _driver = chrome(True)
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
def chrome_browser():
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def page(chrome_browser):
    return HillelHomePage(chrome_browser)


@pytest.fixture
def open_page(page):
    def _open_page():
        page.open_page(HOME_URL)

    return _open_page


@pytest.fixture
def open_form_registration(page):
    def _open_form_registration():
        page.click_element(page.sign_up_button)
        page.find_element(page.registration_popup)

    return _open_form_registration


@pytest.fixture
def fill_form_registration_and_send(page, chrome_browser):
    def _fill_popup_fields(name, last_name, email, password, repeat_password):
        page.fill_input(page.sign_up_name_input, name)
        page.fill_input(page.sign_up_last_name_input, last_name)
        page.fill_input(page.sign_up_email_input, email)
        page.fill_input(page.sign_up_password_input, password)
        page.fill_input(page.sign_up_repeat_password_input, repeat_password)
        return chrome_browser.current_url

    return _fill_popup_fields


@pytest.fixture
def send_form_registration(page):
    def _send_form_registration():
        page.click_element(page.register_button)

    return _send_form_registration


@pytest.fixture
def check_switch_to_garage_page(chrome_browser):
    def _check_switch_to_garage_page():
        page = HillelGaragePage(chrome_browser)
        assert page.find_element(page.add_car_button)
        assert chrome_browser.current_url == GARAGE_URL

    return _check_switch_to_garage_page
