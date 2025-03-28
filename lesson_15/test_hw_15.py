import pytest
from hw_15 import Rhombus

def test_valid_rhombus():
    rhombus = Rhombus(10, 100)
    assert rhombus.side_a == 10
    assert rhombus.angle_a == 100
    assert rhombus.angle_b == 80

def test_invalid_side():
    with pytest.raises(ValueError, match="Side_a must be greater than 0"):
        Rhombus(0, 60)
    with pytest.raises(ValueError, match="Side_a must be greater than 0"):
        Rhombus(-5, 120)

def test_invalid_angle():
    with pytest.raises(ValueError, match="Angle_a must be between 0 and 180"):
        Rhombus(6, 180)
    with pytest.raises(ValueError, match="Angle_a must be between 0 and 180"):
        Rhombus(10, 0)
    with pytest.raises(ValueError, match="Angle_a must be between 0 and 180"):
        Rhombus(4, -19)

def test_angle_update():
    rhombus = Rhombus(9, 55)
    rhombus.angle_a = 30
    assert rhombus.angle_b == 150
    rhombus.angle_a = 75
    assert rhombus.angle_b == 105

def test_str_display():
    rhombus = Rhombus(10, 120)
    assert str(rhombus) == "Rhombus: side a = 10, angle a = 120°, angle b = 60°."

if __name__ == "__main__":
    pytest.main(["-v", __file__])