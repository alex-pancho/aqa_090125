import unittest
try:
    from homework_08 import sum_of_numbers
except ImportError:
    from homework_08 import sum_of_numbers

class TestSumNumbersInList(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(sum_of_numbers(['1,2,3', '4,0,6']), [6, 10])
        self.assertEqual(sum_of_numbers(['1,2,3,4', '1,2,3,4,50']), [10, 60])

    def test_invalid_strings(self):
        self.assertEqual(sum_of_numbers(['1,2,3', '4/0,6', 'asas7,8,9']), [6, 'Не можу це зробити! ValueError', 'Не можу це зробити! ValueError'])
        self.assertEqual(sum_of_numbers(['1,2,3', 'asas7,8,9', '4,0,6']), [6, 'Не можу це зробити! ValueError', 10])

    def test_non_string_elements(self):
        self.assertEqual(sum_of_numbers(['1,2,3', 7]), [6, 'Не можу це зробити! Not a string'])
        self.assertEqual(sum_of_numbers(["1,2,3,4", "1,2,3,4,50", sum, min(1,2)]), [10, 60, 'Не можу це зробити! Not a string', 'Не можу це зробити! Not a string'])

    def test_empty_list(self):
        self.assertEqual(sum_of_numbers([]), 'Список порожній')

    def test_non_list_input(self):
        self.assertEqual(sum_of_numbers('21'), 'Not a list')
        self.assertEqual(sum_of_numbers(3), 'Not a list')

    def test_mixed_valid_invalid(self):
        self.assertEqual(sum_of_numbers(
            ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3",
             {'country':'Ukraine', 'continent': 'Europe', 'size': 123}
            ]), 
            [10, 60, 'Не можу це зробити! ValueError', 'Не можу це зробити! Not a string'])

if __name__ == '__main__':
    unittest.main()