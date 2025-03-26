import pytest
import logging
from homework_18 import factorial, factorial_generator

# Configure logging for tests (optional, but good practice)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_factorial_positive_integer():
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(1) == 1

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_generator_sequence():
    generated_factorials = list(factorial_generator(5))
    expected_factorials = [1, 1, 2, 6, 24, 120]
    assert generated_factorials == expected_factorials

def test_factorial_generator_logging_output(caplog):
    n = 2
    expected_logs = [
        "Факторіал від 0! = 1",
        "Факторіал від 1! = 1",
        "Факторіал від 2! = 2",
    ]
    with caplog.at_level(logging.INFO):
        list(factorial_generator(n))
        logged_messages = [record.getMessage() for record in caplog.records if record.levelname == 'INFO']
        assert len(logged_messages) == len(expected_logs)
        for i in range(len(expected_logs)):
            assert expected_logs[i] in logged_messages[i]
