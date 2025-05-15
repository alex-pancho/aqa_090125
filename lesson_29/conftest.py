import pytest

from db import delete_result


@pytest.fixture(scope="session")
def clean_db():
    yield
    delete_result()
