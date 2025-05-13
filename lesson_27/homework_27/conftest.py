import pytest
from selenium.webdriver import Chrome

@pytest.fixture
def browser_chrome():
    driver = Chrome()
    yield driver
    driver.quit()
    