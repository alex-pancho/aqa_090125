import pytest
from hw_15 import Rhombus

@pytest.fixture(scope='class')
def instance():
    return Rhombus(side=10, angle_a=35)

class TestRhombus:
    def test_creating_rhombus(self, instance):
        assert instance.side == 10
        assert instance.angle_a == 35
        assert instance.angle_b == 180 - instance.angle_a

    def test_rhombus_str_method(self, instance):
        expected_result = f"Rhombus parameters: side=10, angleA=35, angleB=145"
        assert str(instance) == expected_result


    def test_setting_attributes_positive(self, instance):
        instance.side = 20
        instance.angle_a = 21.5
        assert instance.side == 20
        assert instance.angle_a == 21.5
        assert instance.angle_b == 180 - instance.angle_a

    def test_setting_attributes_negative(self, instance):
        with pytest.raises(ValueError):
            instance.side = -10

    def test_creating_rhombus_with_corrupted_data(self):
        with pytest.raises(ValueError):
            Rhombus(side=0, angle_a=35)
        with pytest.raises(ValueError):
            Rhombus(side=10, angle_a=185)
        with pytest.raises(TypeError):
            Rhombus(side='10', angle_a=35)

    def test_creating_rhombus_with_no_params(self):
        with pytest.raises(TypeError):
            Rhombus()

    def test_calling_instance_with_undefined_attribute(self, instance):
        with pytest.raises(AttributeError):
            instance.new_attrib