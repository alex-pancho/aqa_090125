import pytest
from get_browser import firefox, chrome

@pytest.fixture
def browser():
    _driver = firefox()
    yield _driver
    _driver.quit()
