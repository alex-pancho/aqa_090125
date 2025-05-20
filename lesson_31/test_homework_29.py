import pytest
from homework_29 import perform_operation


def test_add_operations():
    assert perform_operation('add', 1, 1) == 2
    assert perform_operation('add', 6, 5) == 11
    assert perform_operation('add', -1, 1) == 0
    assert perform_operation('add', 0, 0) == 0


def test_subtract_operations():
    assert perform_operation('subtract', 5, 3) == 2
    assert perform_operation('subtract', 0, 3) == -3
    assert perform_operation('subtract', 10, 10) == 0
    assert perform_operation('subtract', -5, -3) == -2


def test_multiply_operations():
    assert perform_operation('multiply', 3, 4) == 12
    assert perform_operation('multiply', 5, 5) == 25
    assert perform_operation('multiply', 0, 100) == 0
    assert perform_operation('multiply', -2, 3) == -6


def test_divide_operations():
    assert perform_operation('divide', 10, 2) == 5
    assert perform_operation('divide', 6, 12) == 0.5
    assert perform_operation('divide', 1, 2) == 0.5
    assert perform_operation('divide', -10, 2) == -5

    with pytest.raises(ValueError, match='Division by zero'):
        perform_operation('divide', 10, 0)


def test_unknown_operation():
    with pytest.raises(ValueError, match='Unknown operation'):
        perform_operation('power', 2, 3)
    with pytest.raises(ValueError, match='Unknown operation'):
        perform_operation('', 2, 3)
    with pytest.raises(ValueError, match='Unknown operation'):
        perform_operation(None, 2, 3)