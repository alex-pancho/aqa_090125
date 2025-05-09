import pytest

from selenium.webdriver import Chrome

from homework_28.hw_pages.hw_home_page import HomePageHillel
from homework_28.hw_pages.hw_garage_page import GaragePage


HOME_URL = "https://guest:welcome2qauto@qauto2.forstudy.space"
GARAGE_URL = "https://guest:welcome2qauto@qauto2.forstudy.space/panel/garage"


@pytest.fixture
def chrome_browser():
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def page(chrome_browser):
    return HomePageHillel(chrome_browser)


@pytest.fixture
def open_page(page):
    def _open_page():
        page.open_page(HOME_URL)

    return _open_page


@pytest.fixture
def open_registration_popup(page):
    def _open_registration_popup():
        page.click_button(page.sign_up_button)

    return _open_registration_popup


@pytest.fixture
def fill_registration_popup(page):
    def _fill_fields(name, last_name, email, password, repeat_password):
        page.fill_input(page.sign_up_name_input, name)
        page.fill_input(page.sign_up_last_name_input, last_name)
        page.fill_input(page.sign_up_email_input, email)
        page.fill_input(page.sign_up_password_input, password)
        page.fill_input(page.sign_up_repeat_password_input, repeat_password)

    return _fill_fields


@pytest.fixture
def send_registration_popup(page):
    def _send_registration_popup():
        page.click_button(page.register_button)

    return _send_registration_popup


@pytest.fixture
def check_switch_to_garage_page(chrome_browser):
    def _check_switch_to_garage_page():
        page = GaragePage(chrome_browser)
        assert page.find_element(page.add_car_button)
        assert page.find_element(page.titele)
        assert chrome_browser.current_url == GARAGE_URL

    return _check_switch_to_garage_page
