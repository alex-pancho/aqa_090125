import unittest
try:
    from lesson_08.homework_08 import sum_numbers_in_list
except ImportError:
    from homework_08 import sum_numbers_in_list

class TestSumNumbersInList(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(sum_numbers_in_list(['1,2,3', '4,0,6']), [6, 10])
        self.assertEqual(sum_numbers_in_list(['1,2,3,4', '1,2,3,4,50']), [10, 60])

    def test_invalid_strings(self):
        self.assertEqual(sum_numbers_in_list(['1,2,3', '4/0,6', 'asas7,8,9']), [6, 'Не можу це зробити! ValueError', 'Не можу це зробити! ValueError'])
        self.assertEqual(sum_numbers_in_list(['1,2,3', 'asas7,8,9', '4,0,6']), [6, 'Не можу це зробити! ValueError', 10])

    def test_non_string_elements(self):
        self.assertEqual(sum_numbers_in_list(['1,2,3', 7]), [6, 'Не можу це зробити! AttributeError'])
        self.assertEqual(sum_numbers_in_list(["1,2,3,4", "1,2,3,4,50", sum, min(1,2)]), [10, 60, 'Не можу це зробити! AttributeError', 'Не можу це зробити! AttributeError'])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            sum_numbers_in_list([])

    def test_non_list_input(self):
        with self.assertRaises(ValueError):
            sum_numbers_in_list('21')
        with self.assertRaises(ValueError):
            sum_numbers_in_list(3)

    def test_mixed_valid_invalid(self):
        self.assertEqual(sum_numbers_in_list(
            ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3",
             {'country':'Ukraine', 'continent': 'Europe', 'size': 123}
            ]), 
            [10, 60, 'Не можу це зробити! ValueError', 'Не можу це зробити! AttributeError'])

if __name__ == '__main__':
    unittest.main()