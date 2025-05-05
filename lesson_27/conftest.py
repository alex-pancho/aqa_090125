import pytest
from get_browser import chrome

@pytest.fixture
def browser():
    _driver = chrome()
    yield _driver
    _driver.quit()
