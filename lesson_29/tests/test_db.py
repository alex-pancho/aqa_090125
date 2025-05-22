import pytest
import logging
import allure

from app.db import insert_result, update_result, fetch_results, delete_result, db_cursor
from app.operations import add, subtract, multiply, divide
from tests.logger_config import configure_logging

configure_logging()

@allure.feature("Database Insert")
@allure.story("Add new entry")
def test_insert():
    with allure.step("Insert result into DB"):
        insert_result("test_add", 2, 2, 4)

    with allure.step("Check if result is inserted"):
        with db_cursor() as cursor:
            cursor.execute("SELECT * FROM results WHERE operation='test_add'")
            rows = cursor.fetchall()
            assert len(rows) >= 1
            logging.info("test_insert passed with rows: %s", rows)

@allure.feature("Database Update")
@allure.story("Update entry")
def test_update():
    with allure.step("Insert initial result"):
        insert_result("test_add", 2, 2, 4)

    with allure.step("Update result"):
        update_result("test_add", 10)

    with allure.step("Check if result was updated"):
        with db_cursor() as cursor:
            cursor.execute("SELECT result FROM results WHERE operation='test_add'")
            result = cursor.fetchone()[0]
            assert float(result) == 10.0
            logging.info("test_update passed with result: %s", result)

@allure.feature("Database Fetch")
@allure.story("Retrieve records")
def test_fetch():
    with allure.step("Fetch all results"):
        results = fetch_results()
        assert isinstance(results, list)
        assert any(r[1] == "test_add" for r in results)
        logging.info("test_fetch passed with results count: %d", len(results))

@allure.feature("Database Delete")
@allure.story("Remove entry")
def test_delete():
    with allure.step("Delete test_add record"):
        delete_result("test_add")

    with allure.step("Verify deletion"):
        with db_cursor() as cursor:
            cursor.execute("SELECT * FROM results WHERE operation='test_add'")
            rows = cursor.fetchall()
            assert len(rows) == 0
            logging.info("test_delete passed")

@allure.feature("Math Operations")
@allure.story("Basic arithmetic")
def test_math_operations():
    with allure.step("Test add"):
        assert add(2, 3) == 5
    with allure.step("Test subtract"):
        assert subtract(5, 2) == 3
    with allure.step("Test multiply"):
        assert multiply(4, 5) == 20
    with allure.step("Test divide"):
        assert divide(8, 2) == 4.0
    logging.info("test_math_operations passed")