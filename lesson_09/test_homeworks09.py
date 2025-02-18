import unittest

try:
    from lesson_09.homeworks import longest_word_in_list
    from lesson_09.homeworks import solution_for_diff_in_dicts
    from lesson_09.homeworks import multiplication_table
except ImportError:
    from homeworks import longest_word_in_list
    from homeworks import solution_for_diff_in_dicts
    from homeworks import multiplication_table

class TestMultiplTable(unittest.TestCase):

    def test_01_positive_check_multiply(self):
        """Positive check"""
        self.assertEqual(longest_word_in_list(['what', 'is', 'longest', 'word']), "longest")
        self.assertEqual(longest_word_in_list(['one', 'two', 'three', 'sixteen']), "sixteen")
    
    def test_02_empty_list(self):
        """Negative check with empty list"""
        with self.assertRaises(TypeError):
            longest_word_in_list([])

    def test_03_el_in_list_not_str(self):
        """Negative check with empty list"""
        with self.assertRaises(TypeError):
            longest_word_in_list([123, 'some', 'word'])

    def test_04_is_not_list(self):
        """Negative check for input is not a list"""
        with self.assertRaises(TypeError):
            longest_word_in_list(123)

    def test_05_positive_check_dict_difference_of_values(self):
        """Positive check for difference of values in two dicts"""
        self.assertEqual(solution_for_diff_in_dicts({'Анна Коваленко': 92, 'Олег Петров': 85, 'Ірина Сидорова': 78}, {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 80}), {'Анна Коваленко': 2, 'Олег Петров': 0, 'Ірина Сидорова': -2})
        self.assertEqual(solution_for_diff_in_dicts({'Olha Syn': 94, 'Artem Petr': 83, 'Vasyl Ukr': 74, 'Max Lyvs': 100}, {'Olha Syn': 90, 'Artem Petr': 80, 'Vasyl Ukr': 72, 'Max Lyvs': 98}), {'Olha Syn': 4, 'Max Lyvs': 2, 'Artem Petr': 3, 'Vasyl Ukr': 2})
    
    def test_06_negative_check_dict_without_value(self):
        """Negative check without value in one of dicts"""
        with self.assertRaises(TypeError):
            solution_for_diff_in_dicts({'Анна Коваленко'}, {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 80}, {'Анна Коваленко': 2, 'Олег Петров': 0, 'Ірина Сидорова': -2})

    def test_07_negative_check_empty_dict(self):
        """Negative check without similar key"""
        with self.assertRaises(AttributeError):
            solution_for_diff_in_dicts({'Анна Коваленко': 92, 'Олег Петров': 85, 'Ірина Сидорова': 78}, {'Олег Петров': 85, 'Ірина Сидорова': 78})

    def test_08_positive_check_multiple_table(self):
        """"Positive check for multible table"""
        self.assertEqual(multiplication_table(3, 3), '1 x 3 = 3\n2 x 3 = 6\n3 x 3 = 9')
        self.assertEqual(multiplication_table(2, 5), '1 x 2 = 2\n2 x 2 = 4\n3 x 2 = 6\n4 x 2 = 8\n5 x 2 = 10')

    def test_09_negative_check_multiple_table_without_one_arg(self):
        """"Negative check for multiple table without one of args"""
        with self.assertRaises(ValueError):
            multiplication_table(5)

    def test_10_negative_check_multiple_taple_args_not_int(self):
        """"Negative check for multiple table where args not ints"""
        with self.assertRaises(TypeError):
            multiplication_table(5, "two")


if __name__ == "__main__":
    unittest.main(verbosity=2)
