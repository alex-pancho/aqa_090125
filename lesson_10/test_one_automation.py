import pytest
import os

def sum(a, b):
    return a + b


@pytest.mark.smoke
def test_sum():
    """Test the sum function."""
    c = sum(3, 4)
    expected = 7
    assert c == expected, f"Expected value: {expected}"
    assert isinstance(c, int)
    #assert True  #NONSENSE!


def test_example():
    x = 5
    y = 10
    if x + y != 11:
        pytest.fail("Помилка: Сума x та y не дорівнює 11")


def test_example_2():
    result = 32
    if result != 23:
        pytest.xfail("Очікуваний результат не співпадає з отриманим")


@pytest.mark.skip(reason="Причина пропуску тесту")
def test_skip():
    assert False

def check_os_is_windows():
    return os.name == "nt"


@pytest.mark.skipif(check_os_is_windows(), reason="Причина пропуску тесту")
def test_skip_nt():
    assert False

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as exc_info:
        10/0
    assert str(exc_info.value) == "division by zero"
    