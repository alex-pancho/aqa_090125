from homework_08 import sum_numbers_in_list
import unittest

class TestSumNumbersInList(unittest.TestCase):

    def test_01_valid_input(self):
        """ Тест на коректні вхідні дані """
        actual_result = sum_numbers_in_list(["1,2,3", "4,0,6"])
        expected_result = [6, 10]
        self.assertEqual(actual_result, expected_result)
        actual_result = sum_numbers_in_list(["1,2,3,4", "1,2,3,4,50"])
        expected_result = [10, 60]
        self.assertEqual(actual_result, expected_result)

    def test_02_invalid_strings(self):
        """ Тест на некоректні типи даних всердині строки """
        self.assertEqual(
            sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"]),
            [6, "Не можу це зробити!", "Не можу це зробити!"],
        )
        self.assertEqual(
            sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]),
            [6, "Не можу це зробити!", 10],
        )

if __name__ == "__main__":
    unittest.main(verbosity=2)
