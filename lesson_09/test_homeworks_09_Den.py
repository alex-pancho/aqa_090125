import unittest

from aqa_local_repo.aqa_090125.lesson_08.homework_08 import sum_numbers_in_list
from homework_09_Den import count_vowels, compare_grades, sum_positive_numbers

class TestHomework09(unittest.TestCase):
    """Тесты для подсчета гласных в строке"""
    def test_string_with_vowels(self):
        self.assertEqual(count_vowels("Python is awesome!"), {'o': 2, 'i': 1, 'a': 1, 'e': 2, 'y': 1})

    def test_no_vowels_string(self):
        self.assertEqual(count_vowels("bcdfg"), {})

    def test_insensitivity_to_case(self):
        self.assertEqual(count_vowels("AEIOUYaeiouy"), {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2, 'y': 2})

    """Тесты для для сравнения оценок студентов"""
    def test_routine_positive_check(self):
        self.assertEqual(compare_grades({'Анна': 90, 'Ваня': 89}, {'Анна': 85, 'Ваня': 87}), {'Анна': 5, 'Ваня': 2})

    def test_student_is_missing_g1(self):
        self.assertEqual(compare_grades({'Анна': 90},{'Анна': 85, 'Ваня': 87}), {'Ваня': 87, 'Анна': 5})

    def test_student_is_missing_g2(self):
        self.assertEqual(compare_grades({'Анна': 90, 'Ваня': 89},{'Анна': 90}), {'Анна': 0, 'Ваня': 89})

    """Тесты для суммирования чисел в списке"""
    def test_positive_numbers(self):
        self.assertEqual(sum_positive_numbers([1, 2, 3, 4]), 10)

    def test_positive_and_negative_numbers(self):
        self.assertEqual(sum_positive_numbers([0, -1, 5, -2, 10]), 15)

    def test_empty_list(self):
        self.assertEqual(sum_positive_numbers([]), 0)

    """Негативные проверки"""
    def test_invalide_type(self):
        with self.assertRaises(ValueError):
            sum_positive_numbers("123")
        with self.assertRaises(ValueError):
            sum_positive_numbers(123)
        with self.assertRaises(ValueError):
            sum_positive_numbers({'a': 1})

if __name__ == "__main__":
    unittest.main()
