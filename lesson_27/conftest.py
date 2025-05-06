import pytest
from get_browser import firefox, chrome
from selenium.webdriver import Chrome

@pytest.fixture
def browser():
    _driver = firefox()
    yield _driver
    _driver.quit()


@pytest.fixture
def chrome_browser():
    driver = Chrome()
    yield driver
    driver.quit()
