import pytest
import allure
from app import db

@pytest.fixture(scope="module", autouse=True)
def setup():
    db.init_db()

@allure.feature("Database connection")
def test_connection():
    with allure.step("Connect to database"):
        conn = db.get_connection()
        assert conn is not None
        conn.close()

@allure.feature("Insert operation")
def test_insert_result():
    with allure.step("Insert a record"):
        db.insert_result("add", 5.0)
    with allure.step("Verify record exists"):
        results = db.get_results()
        assert any(r["operation"] == "add" and r["result"] == 5.0 for r in results)
