import logging
from tests.logger_config import configure_logging
from app.db import insert_result, update_result, fetch_results, delete_result
from app.operations import add, subtract, multiply, divide

configure_logging()

def test_insert(db_session):
    db_session.execute("INSERT INTO results (operation, a, b, result) VALUES ('test_add', 2, 2, 4)")
    db_session.execute("SELECT * FROM results WHERE operation='test_add'")
    rows = db_session.fetchall()
    assert len(rows) >= 1
    logging.info("test_insert passed with rows: %s", rows)

def test_update(db_session):
    insert_result("test_add", 2, 2, 4)
    update_result("test_add", 10)
    db_session.execute("SELECT result FROM results WHERE operation='test_add'")
    result = db_session.fetchone()[0]
    assert float(result) == 10.0
    logging.info("test_update passed with result: %s", result)

def test_fetch():
    results = fetch_results()
    assert isinstance(results, list)
    assert any(r[1] == "test_add" for r in results)
    logging.info("test_fetch passed with results count: %d", len(results))

def test_delete(db_session):
    delete_result("test_add")
    db_session.execute("SELECT * FROM results WHERE operation='test_add'")
    rows = db_session.fetchall()
    assert len(rows) == 0
    logging.info("test_delete passed")

def test_math_operations():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(4, 5) == 20
    assert divide(8, 2) == 4.0
    logging.info("test_math_operations passed")