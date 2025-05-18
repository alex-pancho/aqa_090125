import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    """Налаштування драйвера браузера для Pytest."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
