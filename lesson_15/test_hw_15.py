import unittest
from hw_15 import Rhombus

class TestRhombus(unittest.TestCase):

    def test_01_valid_rhombus(self):
        rhombus = Rhombus(5, 60)
        self.assertEqual(str(rhombus), "Rhombus: side_a = 5, angle_a = 60, angle_b = 120")
        self.assertEqual(rhombus.side_a, 5)
        self.assertEqual(rhombus.angle_a, 60)
        self.assertEqual(rhombus.angle_b, 120) 

    def test_02_invalid_side_a(self):
        with self.assertRaises(ValueError) as e:
            rhombus = Rhombus(-5, 60)
        self.assertEqual(str(e.exception), 'Side_a must be greater than 0')

    def test_03_invalid_angle_a(self):
        with self.assertRaises(ValueError) as e:
            rhombus = Rhombus(5, 180)
        self.assertEqual(str(e.exception), 'Angle_a must be between 0 and 180')

    def test_04_zero_side_a(self):
        with self.assertRaises(ValueError) as e:
            rhombus = Rhombus(0, 60)
        self.assertEqual(str(e.exception), 'Side_a must be greater than 0')

    def test_05_zero_angle_a(self):
        with self.assertRaises(ValueError) as e:
            rhombus = Rhombus(5, 0)
        self.assertEqual(str(e.exception), 'Angle_a must be between 0 and 180')


if __name__ == "__main__":
    unittest.main(verbosity=2)