import pytest
from get_browser import firefox, chrome
from selenium.webdriver import Firefox

@pytest.fixture
def browser():
    _driver = firefox()
    yield _driver
    _driver.quit()

@pytest.fixture
def firefox_browser():
    driver = Firefox()
    yield driver
    driver.quit()