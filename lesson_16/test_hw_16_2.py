import unittest
from hw_16_2 import Rectangle, Circle
import math

class TestFigures(unittest.TestCase):
    def test_rectangle(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.get_area(), 50)
        self.assertEqual(rect.get_perimeter(), 30)
    
    def test_circle(self):
        circ = Circle(7)
        self.assertAlmostEqual(circ.get_area(), math.pi * 7 ** 2, places=2)
        self.assertAlmostEqual(circ.get_perimeter(), 2 * math.pi * 7, places=2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
