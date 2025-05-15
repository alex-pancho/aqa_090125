import pytest
import allure

from db import calculate_and_store, get_result, delete_result, update_data
from logger import logger


@pytest.mark.usefixtures("clean_db")
class TestDB:

    @allure.title("Test add action and integration with DB")
    @allure.feature("Add numbers and store into the database")
    def test_add(self):
        with allure.step("Calculate 2 + 3"):
            logger.info("Calculate 2 + 3")
            result = calculate_and_store("add", 2, 3)
            logger.info(f"Result: {result}")

        with allure.step(f"Get {result=} form DB"):
            logger.info(f"Get {result} form DB")
            res = get_result(result)
            logger.info(f"DB {result=}")
        assert res == 5, "Wrong DB result"

    @allure.title("Test sub action and integration with DB")
    @allure.feature("Sub numbers and store into the database")
    def test_sub(self):
        with allure.step("Calculate 5 - 3"):
            logger.info("Calculate 5 - 3")
            result = calculate_and_store("sub", 5, 3)
            logger.info(f"Result: {result}")

        with allure.step(f"Get {result=} from DB"):
            logger.info(f"Get {result=}: from DB")
            res = get_result(result)
            logger.info(f"DB {result=}:")
        assert res == 2, "Wrong DB result"

    @allure.title("Test updating DB data")
    @allure.feature("Updating calculated data and store into the database")
    def test_update_data(self):
        a = 100
        b = 11
        with allure.step(f"Calculate {a} + {b} and store into DB"):
            logger.info(f"Calculate {a} + {b}")
            result = calculate_and_store("sub", a, b)
            logger.info(f"{result}")

        with allure.step("Ger result from DB"):
            res_old = get_result(result)
            logger.info(f"{result=} from DB = {res_old}")
        assert res_old == 89, "Wrong DB result"

        with allure.step(f"Update {res_old=} with params: {a=}, {b=}, op=add"):
            logger.info(f"Update {res_old=} with params: {a=}, {b=}, op=add")
            res_new = update_data(res_old, a, b, "add")
            logger.info(f"Updated DB result = {res_new}")

        with allure.step("Get updated result from DB"):
            res_updated = get_result(res_new)
            logger.info(f"Updated result from DB = {res_updated}")
        assert res_updated == 111, "Wrong DB updated result"

        with allure.step("Check old result is missing into DB"):
            res_old = get_result(result)
            logger.info("Check old result is missing into DB")
        assert not res_old, "Result is not missing int DB"

    @allure.title("Test delete data from DB")
    @allure.feature("Deleting data from the database")
    def test_delete_result(self):
        with allure.step("Calculate and store into DB: 100 + 50"):
            calculate_and_store("sub", 100, 50)

        with allure.step("Delete data from DB"):
            assert delete_result(), "Not all has been deletes"
