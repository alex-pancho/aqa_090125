import unittest

try:
    from lesson_09.homework_09_NP import get_even_numbers, clean_dictionary, is_palindrome
except ImportError:
    from homework_09_NP import get_even_numbers, clean_dictionary, is_palindrome


class TestFunctions(unittest.TestCase):
    def test_get_even_numbers(self):
        self.assertEqual(get_even_numbers([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(get_even_numbers([1, 3, 5]), [])
        self.assertEqual(get_even_numbers([]), [])
        self.assertEqual(get_even_numbers([2, "text", 4, None, 6]), [2, 4, 6])

    def test_clean_dictionary(self):
        self.assertEqual(clean_dictionary({"sum": 1, "count": 2}), {"sum": 1, "count": 2})
        self.assertEqual(clean_dictionary({"sum": None, "count": "null"}), {"sum": 0, "count": 0})
        self.assertEqual(clean_dictionary({"sum": "NaN", "count": "none"}), {"sum": 0, "count": 0})
        self.assertEqual(clean_dictionary({"sum": "NaN", "count": "none"}), {"sum": 0, "count": 0})

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
