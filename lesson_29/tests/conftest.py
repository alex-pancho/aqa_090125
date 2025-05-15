import pytest
from app.db import init_db, db_cursor

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    init_db()

@pytest.fixture
def db_session():
    with db_cursor(commit=True) as cursor:
        yield cursor