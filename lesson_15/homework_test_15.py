import unittest
from hw_15 import Rhombus


class TestRhombus((unittest.TestCase)):
    def test_valid_rhombus(self):
        rhombus = Rhombus(10, 20)
        self.assertEqual(str(rhombus), "Rhombus: side_a=10, angle_a=20, angle_b=160")
        rhombus = Rhombus(15, 90)
        self.assertEqual(str(rhombus), "Rhombus: side_a=15, angle_a=90, angle_b=90")

    def test_invalid_side(self):
        rhombus = Rhombus(0, 20)
        self.assertEqual(str(rhombus), "Invalid Rhombus: missing or incorrect attributes")
        rhombus = Rhombus(-10, 20)
        self.assertEqual(str(rhombus), "Invalid Rhombus: missing or incorrect attributes")

    def test_invalid_angle(self):
        rhombus = Rhombus(10, 180)
        self.assertEqual(str(rhombus), "Invalid Rhombus: missing or incorrect attributes")
        rhombus = Rhombus(10, 0)
        self.assertEqual(str(rhombus), "Invalid Rhombus: missing or incorrect attributes")

    def test_invalid_rhombus(self):
        rhombus = Rhombus(0, 0)
        self.assertEqual(str(rhombus), "Invalid Rhombus: missing or incorrect attributes")
        rhombus = Rhombus(-10, 200)
        self.assertEqual(str(rhombus), "Invalid Rhombus: missing or incorrect attributes")

    def test_angle_sum(self):
        rhombus = Rhombus(10, 20)
        self.assertEqual(rhombus.angle_a + rhombus.angle_b, 180)


if __name__ == '__main__':
    unittest.main()