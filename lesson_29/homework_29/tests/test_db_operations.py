from app.operations import add_numbers, get_result_from_db, delete_result_by_id
from pony.orm import db_session

def test_additionl():
    result = add_numbers(4, 6)
    assert result == 10

def test_retrieval_from_db():
    db_result = get_result_from_db(4, 6)
    assert db_result is not None
    assert db_result.result == 10
    assert db_result.operation == 'add'

def test_deletion_by_id():
    add_numbers(1, 2)

    with db_session:
        record = get_result_from_db(1, 2)
        assert record is not None
        deleted = delete_result_by_id(record.id)
        assert deleted

        record_after = get_result_from_db(1, 2)
        assert record_after is None


