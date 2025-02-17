from homeworks import *
import unittest
from unittest.mock import mock_open, patch


class TestListOfStrings(unittest.TestCase):

    def test_01_valid_input(self):
        """Тест на коректні вхядні дані"""
        actual_result = list_of_strings(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])
        expected_result = ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum']
        self.assertEqual(actual_result, expected_result)

    def test_02_invalid_input(self):
        """Тест на некоректні вхідні дані"""
        with self.assertRaises(ValueError):
            list_of_strings('string')
        with self.assertRaises(ValueError):
            list_of_strings({1:3, 1:4})                  
        with self.assertRaises(ValueError):
            list_of_strings({1, 2, 3})
        with self.assertRaises(ValueError):
            list_of_strings(1)
        with self.assertRaises(ValueError):
            list_of_strings(True)

    def test_03_empty_list(self):
        """Туст на порожній список"""
        with self.assertRaises(ValueError):
            list_of_strings([])
    
    def test_04_without_strings(self):
        """Тест на список без строк"""
        with self.assertRaises(ValueError):
            list_of_strings([1, 2, 3, 4, 5])

    def  test_05_raises(self):
        """Тест на помилку кількості аргументів у функції"""
        with self.assertRaises(TypeError):
            list_of_strings(1, 2, 3)
        

class TestReversedDict(unittest.TestCase):

    def test_06_valid_input(self):
        """Тест на коректні вхядні дані"""
        self.assertEqual(reversed_dict({1: 'a', 2: 'b', 3: 'c'}), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(reversed_dict({'a': 1, 'b': (2, 4, 6), 'c': 3}), {1: 'a', (2, 4, 6): 'b', 3: 'c'})
    
    def test_07_invalid_input(self):
        """Тест на некоректні тип вхідних даних"""
        with self.assertRaises(ValueError):
            reversed_dict('string')
        with self.assertRaises(ValueError):
            reversed_dict([1, 2, 3])
        with self.assertRaises(ValueError):
            reversed_dict(1)
        with self.assertRaises(ValueError):
            reversed_dict(True)

    def test_08_empty_dict(self):
        """Тест на порожній словник"""
        with self.assertRaises(ValueError):
            reversed_dict({})

    def test_09_invalid_type_key(self):
        """Тест на некоректний тип ключа"""
        with self.assertRaises(TypeError):
            reversed_dict({1: 'a', 2: 'b', 3: [1, 2, 3]})
        with self.assertRaises(TypeError):
            reversed_dict({1: 'a', 2: 'b', 3: {1, 2, 3}})
        with self.assertRaises(TypeError):
            reversed_dict({1: 'a', 2: 'b', 3: {1:3}})


class TestAverageOfList(unittest.TestCase):

    def test_10_positive_numbers(self):
        """Тест на список з додатними числами"""
        self.assertEqual(average_of_list([1, 2, 3, 4, 5]), 3)
        self.assertEqual(average_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.5)
    
    def test_11_negative_numbers(self):
        """Тест на список з від'ємними числами"""
        self.assertEqual(average_of_list([-1, -2, -3, -4, -5]), -3)
        self.assertEqual(average_of_list([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -5.5)

    def test_12_mixed_numbers(self):
        """Тест на список з додатними і від'ємними числами"""
        self.assertEqual(average_of_list([-1, 2, -3, 4, -5]), -0.6)
        self.assertEqual(average_of_list([-1, 2, -3, 4, -5, -6, 7, -8, 9, -10]), -1.1)

    def test_13_float_numbers(self):
        """Тест на список з дробовими числами"""
        self.assertAlmostEqual(average_of_list([1.1, 2.2, 3.3, 4.4, 5.5]), 3.3)
        self.assertAlmostEqual(average_of_list([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1]), 5.96)

    def test_14_empty_list(self):
        """Тест на порожній список"""
        with self.assertRaises(ValueError):
            average_of_list([])

    def test_15_non_numeric_values(self):
        """Тест на список із нечисловими значеннями (очікуємо TypeError)"""
        with self.assertRaises(TypeError):
            average_of_list([1, 2, "three", 4])

    def test_16_invalid_type(self):
        """Тест на некоректний тип вхідних даних"""
        with self.assertRaises(TypeError):
            average_of_list('string')
        with self.assertRaises(TypeError):
            average_of_list({1, 2, 3})
        with self.assertRaises(TypeError):
            average_of_list(1)
        with self.assertRaises(TypeError):
            average_of_list(True)


class TestCalculateSumFromFile(unittest.TestCase):


    @patch('builtins.open', mock_open(read_data='1 2 3 4 5 6 7 8 9 10'))
    def test_17_valid_input(self):
        """Тест на коректні вхідні дані"""
        self.assertEqual(calculate_sum_from_file('file.txt'), 55)
    
    @patch('builtins.open', mock_open(read_data='10 20 30'))
    def test_18_valid_input(self):
        """Тест на коректні вхідні дані"""
        self.assertEqual(calculate_sum_from_file('file.txt'), 60)

    @patch('builtins.open', mock_open(read_data='10 a 30'))
    def test_19_invalid_data(self):
        """Тест на некоректні дані у файлі"""
        self.assertEqual(calculate_sum_from_file('file.txt'), 40)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_20_file_not_found(self, mock_file):
        """Тест на відсутність файлу"""
        with self.assertRaises(FileNotFoundError):
            calculate_sum_from_file('file.txt')

    @patch('builtins.open', side_effect=ValueError)
    def test_21_invalid_data(self, mock_file):
        """Тест на некоректні дані у файлі"""
        with self.assertRaises(ValueError):
            calculate_sum_from_file('file.txt')

        
 

if __name__ == "__main__":
    unittest.main(verbosity=2)
