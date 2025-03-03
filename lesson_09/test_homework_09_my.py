import unittest

try:
    from  lesson_09.homework_09 import summ_of_number_items, find_substring, multiplication_table, sum_numbers_in_list, is_duplicates
except ImportError:
    from  homework_09 import summ_of_number_items ,find_substring, multiplication_table, sum_numbers_in_list, is_duplicates

class TestSumNumbersInList(unittest.TestCase):
    def test_01_summ_of_number_items_valid_input(self):
        """" Тест на коректні вхідні дані """
        self.assertEqual(summ_of_number_items([1,2,3,4,5]), 15)
        self.assertEqual(summ_of_number_items([]), 0)

    def test_02_summ_of_number_items_invalid_input(self):
        """" Тест на не коректні вхідні дані """
        self.assertEqual(summ_of_number_items([1,2,'t',4,5]), "Помилка: [1, 2, 't', 4, 5]. Для знаходження суми потрібно, щоб усі введені данні були числами.")
        self.assertEqual(summ_of_number_items([1,2,sum,4,5]), "Помилка: [1, 2, <built-in function sum>, 4, 5]. Серед введених даних є некоректний тип.")

    def test_03_find_substring_valid_input(self):
            """" Тест на коректні вхідні дані """
            self.assertEqual(find_substring("функція, яка приймає два рядки", "ія"), 5)

    def test_04_find_substring_invalid_input(self):
        """" Тест на не коректні вхідні дані """
        self.assertEqual(find_substring("функція, яка приймає два рядки", "dva"), "Рядок: dva не входить в рядок: функція, яка приймає два рядки.")
        self.assertEqual(find_substring("функція, яка приймає два рядки", 3), "Помилка: 3 не є рядком")

    def test_05_multiplication_table_valid_input(self):
        """" Тест на коректні вхідні дані """
        self.assertEqual(multiplication_table(3), 27)

    def test_06_multiplication_table_invalid_input(self):
        """" Тест на не коректні вхідні дані """
        self.assertEqual(multiplication_table(26), 26)

    def test_07_sum_numbers_in_list_valid_input(self):
        """" Тест на коректні вхідні дані """
        self.assertEqual(sum_numbers_in_list(["1,2,3,4", "7"]), [10, 7])
        self.assertEqual(sum_numbers_in_list([]), [])

    def test_08_sum_numbers_in_list_invalid_input(self):
        """" Тест на не коректні вхідні дані """
        self.assertEqual(sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]), [6, 'Не можу це зробити!', 10])

    def test_09_is_duplicates_valid_input(self):
        """" Тест на коректні вхідні дані """
        self.assertTrue(is_duplicates([1,2,3,4,3,2,1]), True)
        self.assertTrue(is_duplicates(['t', 'a', 'b', 'c', 't']), True)

    def test_10_is_duplicates_invalid_input(self):
        """" Тест на не коректні вхідні дані """
        self.assertFalse(is_duplicates([1,2,3,4,6,7,8]), False)
        self.assertFalse(is_duplicates(['t', 'a', 'b', 'c', 'T']), False)


if __name__ == "__main__":
    unittest.main(verbosity=1)
