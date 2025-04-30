import pytest

from hw_15 import Rhombus


@pytest.fixture(scope="class")
def setup():
    return Rhombus(5, 60)


class TestHW15:

    def test_pos_object_output(self, setup):
        assert str(setup) == "Rhombus: side_a=5, angle_a=60, angle_b=120"

    def test_pos_has_attributes(self, setup):
        assert hasattr(setup, "side_a")
        assert hasattr(setup, "angle_a")
        assert hasattr(setup, "angle_b")

    def test_pos_get_attributes(self, setup):
        assert getattr(setup, "side_a") == 5
        assert getattr(setup, "angle_a") == 60
        assert getattr(setup, "angle_b") == 120

    def test_pos_depending_attributes(self, setup):
        setup.angle_b = 160
        assert setup.angle_a == 20

        setup.angle_a = 160
        assert setup.angle_b == 20

    def test_pos_input_type(self, setup):
        setup.angle_b = 11.1
        assert setup.angle_b == 11.1

        setup.angle_a = 12.2
        assert setup.angle_a == 12.2

        setup.side_a = 15.5
        assert setup.side_a == 15.5

        setup.angle_b = 11
        assert setup.angle_b == 11

        setup.angle_a = 12
        assert setup.angle_a == 12

        setup.side_a = 15
        assert setup.side_a == 15

    def test_neg_angle_a(self, setup):
        with pytest.raises(ValueError):
            setup.angle_a = -1

        with pytest.raises(ValueError):
            setup.angle_a = "5"

        with pytest.raises(ValueError):
            setup.angle_a = 0

        with pytest.raises(ValueError):
            setup.angle_a = 180

    def test_neg_angle_b(self, setup):
        with pytest.raises(ValueError):
            setup.angle_b = -1

        with pytest.raises(ValueError):
            setup.angle_b = "5"

        with pytest.raises(ValueError):
            setup.angle_b = 0

        with pytest.raises(ValueError):
            setup.angle_b = 180

    def test_neg_side_a(self, setup):
        with pytest.raises(ValueError):
            setup.side_a = -1

        with pytest.raises(ValueError):
            setup.side_a = 0

        with pytest.raises(ValueError):
            setup.side_a = "5"
