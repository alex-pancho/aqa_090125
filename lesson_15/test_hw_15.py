import unittest
from hw_15 import Rhombus


class TestRhombus(unittest.TestCase):
    def test_valid_rhombus(self):
        rhombus = Rhombus(5, 60)
        self.assertEqual(rhombus.side_a, 5)
        self.assertEqual(rhombus.angle_a, 60)
        self.assertEqual(rhombus.angle_b, 120)

    def test_invalid_side(self):
        with self.assertRaises(ValueError):
            Rhombus(0, 60)

    def test_invalid_angle(self):
        with self.assertRaises(ValueError):
            Rhombus(5, 180)

        with self.assertRaises(ValueError):
            Rhombus(5, -10)

    def test_str_representation(self):
        rhombus = Rhombus(4, 75)
        self.assertEqual(str(rhombus), "Rhombus: side = 4, angle_a = 75, angle_b = 105")

class TestRhombusSetattr(unittest.TestCase):
    def test_setattr_valid_side(self):
        rhombus = Rhombus(5, 60)
        rhombus.side_a = 10
        self.assertEqual(rhombus.side_a, 10)

    def test_setattr_invalid_side(self):
        rhombus = Rhombus(5, 60)
        with self.assertRaises(ValueError):
            rhombus.side_a = 0

    def test_setattr_valid_angle(self):
        rhombus = Rhombus(5, 60)
        rhombus.angle_a = 70
        self.assertEqual(rhombus.angle_a, 70)
        self.assertEqual(rhombus.angle_b, 110)

    def test_setattr_invalid_angle(self):
        rhombus = Rhombus(5, 60)
        with self.assertRaises(ValueError):
            rhombus.angle_a = 180
        with self.assertRaises(ValueError):
            rhombus.angle_a = -10

if __name__ == "__main__":
    unittest.main(verbosity=2)
