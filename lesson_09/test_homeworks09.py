import unittest

from homeworks import average_number, longest_word, calculate_total_cost, reverse_string, is_even

"""
Функція, яка розрахує середнє арифметичне списку чисел.
"""
class TestAverageNumber(unittest.TestCase):
    def test_01_average_positive_numbers(self):
        self.assertEqual(average_number([5, 6, 7]), 6)

    def test_02_average_number_negative_numbers(self):
        self.assertEqual(average_number([-5, -8, -14]), -9)

    def test_03_average_number_mixed_numbers(self):
            self.assertEqual(average_number([-5, 8, -14, 0, 77]), 13.2)

    def test_04_average_number_zero_numbers(self):
        self.assertEqual(average_number([0, 0, 0, 0]), 0)

    def test_05_average_number_single_number(self):
            self.assertEqual(average_number([5]), 5)

    def test_06_average_number_float_numbers(self):
            self.assertEqual(average_number([5.0, 4.2, 5.5, -8.0]), 1.675)

    def test_07_average_number_empty_list(self):
          with self.assertRaises(ZeroDivisionError):
            average_number([])

    def test_08_negative_average_number(self):
          with self.assertRaises(TypeError): 
            average_number({"a": 1, "b": 2}) # dict instead of list

          with self.assertRaises(TypeError): # string instead of int
            average_number("typo")
          
          with self.assertRaises(TypeError): # valid and invalid input values
            average_number("5", 56, 4)

""" 
Функція, яка приймає список слів та повертає найдовше слово у списку.
"""
class TestLongestWord(unittest.TestCase):
    def test_01_longest_word(self):
        self.assertEqual(longest_word(["New York", "Los Angeles", "Kyiv", "Porto"]), "Los Angeles")

    def test_02_longest_single(self):
        self.assertEqual(longest_word(["New York"]), "New York")

    def test_03_longest_same_len(self):
        self.assertEqual(longest_word(["cat", "dog", "bat", "cup"]), "cat")

    def test_04_longest_diff_cases(self):
            self.assertEqual(longest_word(["CAT", "Dogs", "bat", "cUppUchIno"]), "cUppUchIno")

    def test_05_longest_empty_string(self):
            self.assertEqual(longest_word(["New York", "", "Kyiv", "Porto"]), "New York")

    def test_07_longest_word_negative_inputs(self):
            with self.assertRaises(ValueError): # empty list
                longest_word([])

            with self.assertRaises(TypeError): # integer instead of string
                longest_word(["New York", 125, "Kyiv", "Porto"])

            with self.assertRaises(TypeError): # string instead of list
                longest_word("New York and Porto")

""" 
Функція обчислює загальну вартість замовлення.
"""
class TestTotalCoast(unittest.TestCase):
    def test_01_total_coast(self):
        self.assertEqual(calculate_total_cost([
    ("Піца велика", 4, 274),
    ("Піца середня", 2, 218),
    ("Сік", 4, 35),
    ("Торт", 1, 350),
    ("Вода", 3, 21)
]), 2085)
        
    def test_02_total_coast_empty_list(self):
        self.assertEqual(calculate_total_cost([]), 0)

    def test_03_total_coast_negative(self):
        with self.assertRaises(TypeError): # wrong number of arguments
            calculate_total_cost([
    ("Піца велика", 4, ),
    ("Піца середня", 2, 218),
    ("Сік", 4, 35)
])
            
        with self.assertRaises(TypeError): # negative number value
            calculate_total_cost([
    ("Піца велика", 4, 274),
    ("Піца середня", -2, 218),
    ("Сік", 4, 35)
])
            
""" 
Функція, яка приймає рядок та повертає його у зворотному порядку.
"""
class TestReverseString(unittest.TestCase):
    def test_01_reverse_string(self):
        self.assertEqual(reverse_string("Прочитай цей рядок у зворотному порядку!"),
         "!укдяроп умонторовз у кодяр йец йатичорП")

    def test_02_reverse_string_negative_cases(self):
        with self.assertRaises(TypeError): #integer instaed of string
             reverse_string(5)

        with self.assertRaises(KeyError):
             reverse_string({5: 'a', 6: 'b'}) # dict instead of string

"""
Функція перевіряє, чи є число парним.
"""
class TestIsEvenNumber(unittest.TestCase):
    def test_01_is_even_number(self):
        self.assertTrue(is_even(96))
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(-24))

    def test_02_is_odd_number(self):
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(333))
        self.assertFalse(is_even(55))

    def test_02_is_even_missing_arguments(self):
         with self.assertRaises(TypeError):
            is_even()

if __name__ == "__main__":
    unittest.main(verbosity=2)        