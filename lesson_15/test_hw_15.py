import pytest
from hw_15 import Rhombus

def test_valid_rhombus():
    rhombus = Rhombus(5, 60)
    assert rhombus.side_a == 5
    assert rhombus.angle_a == 60
    assert rhombus.angle_b == 120

def test_invalid_side_a():
    with pytest.raises(ValueError) as e:
        Rhombus(-1, 60)
    assert str(e.value) == "Довжина сторони має бути більше 0"

def test_invalid_angle_a_less_than_0():
    with pytest.raises(ValueError) as e:
        Rhombus(5, -1)
    assert str(e.value) == "Кут має бути від 0 до 180"

def test_invalid_angle_a_greater_than_180():
    with pytest.raises(ValueError) as e:
        Rhombus(5, 181)
    assert str(e.value) == "Кут має бути від 0 до 180"

def test_cannot_set_angle_b():
    rhombus = Rhombus(5, 60)
    with pytest.raises(AttributeError) as e:
        rhombus.angle_b = 100
    assert str(e.value) == "Не можна задати кут b"