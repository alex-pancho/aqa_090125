import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from homework_29 import perform_operation, get_all_results
from database import create_table

@pytest.fixture(scope='module', autouse=True)
def setup_db():
    create_table()
    yield

def test_add_operations():
    res_add = perform_operation('add', 1, 1)
    assert res_add == 2
    res_add = perform_operation('add', 6, 5)
    assert res_add == 11

def test_subtract_operations():
    res_sub = perform_operation('subtract', 5, 3)
    assert res_sub == 2
    res_sub = perform_operation('subtract', 0, 3)
    assert res_sub == -3

def test_multiply_operations():
    res_mul = perform_operation('multiply', 3, 4)
    assert res_mul == 12
    res_mul = perform_operation('multiply', 5, 5)
    assert res_mul == 25

def test_divide_operations():
    res_div = perform_operation('divide', 10, 2)
    assert res_div == 5
    res_div = perform_operation('divide', 6, 12)
    assert res_div == 0.5

    with pytest.raises(ValueError):
        perform_operation('divide', 10, 0)

def test_database_insertion():
    results = get_all_results()
    assert len(results) > 0
    last_record = results[-1]
    assert last_record[1] in ('add', 'subtract', 'multiply', 'divide')