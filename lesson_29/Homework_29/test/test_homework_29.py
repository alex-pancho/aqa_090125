import pytest
from app.homework_29 import perform_operation, get_all_results
from app.database import create_table

@pytest.fixture(scope='module', autouse=True)
def setup_db():
    create_table()
    yield

def test_operations():
    res_add = perform_operation('add', 1, 1)
    assert res_add == 2
    res_sub = perform_operation('subtract', 5, 3)
    assert res_sub == 2
    res_mul = perform_operation('multiply', 3, 4)
    assert res_mul == 12
    res_div = perform_operation('divide', 10, 2)
    assert res_div == 5

    with pytest.raises(ValueError):
        perform_operation('divide', 10, 0)

def test_database_insertion():
    results = get_all_results()
    assert len(results) > 0
    last_record = results[-1]
    assert last_record[1] in ('add', 'subtract', 'multiply', 'divide')