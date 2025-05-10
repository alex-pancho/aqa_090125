import pytest

from lesson_29.db import calculate_and_store, get_result, delete_result, update_data
from lesson_29.logger import logger


@pytest.mark.usefixtures("clean_db")
class TestDB:
    def test_add(self):
        logger.info("Calculate 2 + 3")
        result = calculate_and_store("add", 2, 3)
        logger.info(f"Result: {result}")
        logger.info(f"Get {result=}: form DB")
        res = get_result(result)
        logger.info(f"DB {result=}")
        assert res == 5, "Wrong DB result"

    def test_sub(self):
        logger.info("Calculate 5 - 3")
        result = calculate_and_store("sub", 5, 3)
        logger.info(f"Result: {result}")
        logger.info(f"Get {result=}: from DB")
        res = get_result(result)
        logger.info(f"DB {result=}:")
        assert res == 2, "Wrong DB result"

    def test_update_data(self):
        a = 100
        b = 11
        logger.info(f"Calculate {a} + {b}")
        result = calculate_and_store("sub", a, b)
        logger.info(f"{result}")
        res_old = get_result(result)
        logger.info(f"{result=} from DB = {res_old}")
        assert res_old == 89, "Wrong DB result"
        logger.info(f"Update {res_old=} with params: {a=}, {b=}, op=add")
        res_new = update_data(res_old, a, b, "add")
        logger.info(f"Updated DB result = {res_new}")
        res_updated = get_result(res_new)
        logger.info(f"Updated result from DB = {res_updated}")
        assert res_updated == 111, "Wrong DB updated result"
        res_old = get_result(result)
        logger.info("Check old result is missing into DB")
        assert not res_old, "Result is not missing int DB"

    def test_delete_result(self):
        calculate_and_store("sub", 100, 50)
        assert delete_result(), "Not all has been deletes"
