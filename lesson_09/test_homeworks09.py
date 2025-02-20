import unittest
from homeworks import reverse_string, get_average, price_of_the_item, sum_of_even_numbers

class TestReverseTheString(unittest.TestCase):

    def test_01_valid_input(self):
        """" Тест на коректні вхідні дані """
        self.assertEqual(reverse_string("String to reverse!"), ("!esrever ot gnirtS"))
        self.assertEqual(reverse_string("34565543"), ("34556543"))
        self.assertEqual(reverse_string("123 Lorem Ipsum 9%"), ("%9 muspI meroL 321"))

    def test_02_non_string_input(self):
        """ Тест на некоректний тип вхідних даних """
        with self.assertRaises(TypeError):
            reverse_string(23434)
        with self.assertRaises(TypeError):
            reverse_string(min(1, 2))

class TestAvarageOfTheNumbersList(unittest.TestCase):

    def test_03_valid_input(self):
        """" Тест на коректні вхідні дані """
        self.assertEqual(get_average([18, 2, 65, 25, 3, 34, 8, 83, 74, 5]), (31.7))
        self.assertEqual(get_average([18.5, 2.62, 65.863, 25.61, 3.1, 34.34]), (25.0055))
        self.assertEqual(get_average([-4, -5, -7, -25, -3, -1]), (-7.5))
        self.assertEqual(get_average([-4, 15, -7.63, 25.54, 0, 55]), (13.985))

    def test_04_non_list_input(self):
        """ Тест на некоректний тип вхідних даних """
        with self.assertRaises(TypeError):
            get_average(22)
        with self.assertRaises(TypeError):
            get_average(min(1, 2))
        with self.assertRaises(TypeError):
            get_average(("one, two"))
        with self.assertRaises(TypeError):
            get_average(({"country": "Ukraine", "continent": "Europe", "size": 123}))

    def test_05_empty_list(self):
        """ Тест на порожній список """
        with self.assertRaises(ZeroDivisionError): #As the length of th list is 0
            get_average([])

class TestCalculatePrice(unittest.TestCase):

    def test_06_valid_input(self):
        """" Тест на коректні вхідні дані """
        self.assertEqual(price_of_the_item(1179, 18), (21222))
        self.assertEqual(price_of_the_item(100, 18), (1800))
        self.assertEqual(price_of_the_item(434.74, 46), (19998.04))

    def test_07_empty_input(self):
        """ Тест на порожній список """
        with self.assertRaises(TypeError):
            price_of_the_item(())

    def test_08_invalid_input(self):
        """ Тест на некоректний тип вхідних даних """
        with self.assertRaises(TypeError):
            price_of_the_item(({"country": "Ukraine", "continent": "Europe", "size": 123}))
        with self.assertRaises(TypeError):
            price_of_the_item(("test", {"country": "Ukraine"}))
        with self.assertRaises(TypeError):
            price_of_the_item(("test", "one"))
        with self.assertRaises(TypeError):
            price_of_the_item((223))

class TestCalculateSumOfEvenNumbers(unittest.TestCase):

    def test_09_valid_input(self):
        """" Тест на коректні вхідні дані """
        self.assertEqual(sum_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15]), (42))
        self.assertEqual(sum_of_even_numbers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -15]), (-42))
        self.assertEqual(sum_of_even_numbers([1, 3, 5, 7, 9, 1, 11, 1, 13, 15]), (0))
        self.assertEqual(sum_of_even_numbers([2, 4, 6, 8, 10]), (30))
  
    def test_10_invalid_input(self):
        """ Тест на некоректний тип вхідних даних """
        with self.assertRaises(TypeError):
            sum_of_even_numbers((223))
        with self.assertRaises(TypeError):
            sum_of_even_numbers(("2, 4, 6, 8, 10"))
        with self.assertRaises(TypeError):
            sum_of_even_numbers()
       
       
if __name__ == "__main__":
    unittest.main(verbosity=2)
