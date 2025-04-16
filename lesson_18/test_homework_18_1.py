import unittest
from io import StringIO
import sys
from homework_18_1 import factorial, factorial_generator


class TestFactorialFunctionality(unittest.TestCase):
    def test_factorial_values(self):
        expected = [1, 1, 2, 6, 24, 120]
        result = [factorial(i) for i in range(6)]
        self.assertEqual(result, expected)

    def test_generator_output(self):
        expected = [1, 1, 2, 6, 24, 120]
        self.assertEqual(list(factorial_generator(5)), expected)

    def test_logging_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        factorial(3)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Calling factorial(3)", output)
        self.assertIn("Result: 6", output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
