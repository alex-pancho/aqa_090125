import unittest
import logging
from homework_18_1 import factorial, factorial_generator

class TestFactorialFunctions(unittest.TestCase):
    
    def test_factorial_values(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)

    def test_factorial_generator_output(self):
        expected = [1, 1, 2, 6, 24, 120]
        result = list(factorial_generator(5))
        self.assertEqual(result, expected)

    def test_logging_output(self):
        with self.assertLogs(level=logging.INFO) as cm:
            list(factorial_generator(2))

        logs = '\n'.join(cm.output)
        self.assertIn("Calling factorial(0)", logs)
        self.assertIn("Result: 1", logs)
        self.assertIn("Calling factorial(2)", logs)
        self.assertIn("Result: 2", logs)

if __name__ == '__main__':
    unittest.main(verbosity=2)