import pytest
from app import db

@pytest.fixture(scope="module", autouse=True)
def setup():
    db.init_db()

def test_connection():
    conn = db.get_connection()
    assert conn is not None
    conn.close()

def test_insert_result():
    db.insert_result("test_op", 123.45)
    results = db.get_results()
    assert any(r["operation"] == "test_op" and r["result"] == 123.45 for r in results)

def test_update_result():
    db.insert_result("to_update", 1.0)
    results = db.get_results()
    record = next(r for r in results if r["operation"] == "to_update")
    db.update_result(record["id"], 9.99)
    updated = db.get_results()
    assert any(r["id"] == record["id"] and r["result"] == 9.99 for r in updated)

def test_delete_result():
    db.insert_result("to_delete", 0.0)
    results = db.get_results()
    record = next(r for r in results if r["operation"] == "to_delete")
    db.delete_result(record["id"])
    new_results = db.get_results()
    assert all(r["id"] != record["id"] for r in new_results)

