import unittest
from homework_18 import factorial, factorial_generator


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_generator(self):
        expected_results = [1, 1, 2, 6, 24, 120]
        results = list(factorial_generator(5))
        self.assertEqual(results, expected_results)


if __name__ == '__main__':
    unittest.main()