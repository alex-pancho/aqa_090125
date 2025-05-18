import unittest
from homework_09 import check_string_length, is_valid_email, filter_strings

class TestStringLenght(unittest.TestCase):
    def test_valid_lenght(self):
        self.assertEqual(check_string_length("20 символів111111111"), "Все ок! Довжина рядка від 8 до 20 символів")
        self.assertEqual(check_string_length("11 символів"), "Все ок! Довжина рядка від 8 до 20 символів")
        self.assertEqual(check_string_length("8 символ"), "Все ок! Довжина рядка від 8 до 20 символів")

    def test_too_long(self):
        with self.assertRaises(TypeError):
            check_string_length(["20 символів1111111111"])

    def test_too_short(self):
        with self.assertRaises(TypeError):
            check_string_length(["12"])

    def test_non_string(self):
        with self.assertRaises(TypeError):
            check_string_length(["12", "no", "loooooong"])

class TestValidEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("email@gmail.com"))

    def test_no_valid_email(self):
        self.assertFalse(is_valid_email("email.gmail@com"))
        self.assertFalse(is_valid_email("email@gmailcom"))
        self.assertFalse(is_valid_email("emailgmail.com"))


class TestStringList(unittest.TestCase):
    def test_mix_list(self):
        actual_result = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipso']
        expected_result = ['1', '2', 'False', '6', 'Python', 'Lorem Ipso']
        self.assertEqual(filter_strings(actual_result), expected_result)

    def test_only_strings(self):
        actual_result = ["apple", "banana", "cherry"]
        expected_result = ["apple", "banana", "cherry"]
        self.assertEqual(filter_strings(actual_result), expected_result)

    def test_no_strings(self):
        actual_result = [1, 2, 3, 4.5, None, True, False]
        expected_result = []
        self.assertEqual(filter_strings(actual_result), expected_result)

    def test_empty_list(self):
        actual_result = [1]
        expected_result = []
        self.assertEqual(filter_strings(actual_result), expected_result)


if __name__ == "__main__":
    import unittest
    unittest.main()
