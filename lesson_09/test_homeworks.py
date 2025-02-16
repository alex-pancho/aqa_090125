import unittest

from lesson_09.homeworks import get_sum_of_numbers, do_sum, revers_string, get_common_set_data, sort_people_by_age


class TestSumNumbersInList(unittest.TestCase):

    def test_01_valid_input(self):
        """" Test correct input data type """
        self.assertListEqual(get_sum_of_numbers(["1,2,3", "4,0,6"]), [6, 10])
        self.assertListEqual(get_sum_of_numbers(["1,2,3,4", "1,2,3,4,50"]), [10, 60])

    def test_02_invalid_input(self):
        """ Test incorrect input data type """
        with self.assertRaises(TypeError):
            do_sum([3])
        with self.assertRaises(TypeError):
            do_sum("1234")
        with self.assertRaises(ValueError):
            do_sum([])
        with self.assertRaises(ValueError):
            do_sum(["qwerty123"])

    def test_03_output_type(self):
        """" Test output type """
        self.assertTrue(
            isinstance(get_sum_of_numbers(["1,2,3"]), list),
            f"Output: {type(get_sum_of_numbers(['1,2,3']))} is not a list")

    def test_04_output_sum_value_type(self):
        """" Test output sum value type """
        self.assertTrue(
            isinstance(get_sum_of_numbers(["1,2,3"])[0], int),
            f"Output: {type(get_sum_of_numbers(['1,2,3'])[0])} is not int")


class TesStringReverse(unittest.TestCase):
    def test_05_string_is_reversed(self):
        """" Test reversed string is returned"""
        some_str = "qwerty123"
        self.assertEqual(revers_string(some_str), "321ytrewq")

    def test_06_input_type(self):
        """Test input type is string"""
        with self.assertRaises(TypeError) as e:
            revers_string(123)
        self.assertEqual("Input data is not string", str(e.exception))


class TestSetIntersection(unittest.TestCase):

    def test_07_common_sets_part(self):
        """ Test common sets part"""
        self.assertSetEqual(get_common_set_data({1, 2, 3}, {2, 3, 4}), {2, 3})

    def test_08_input_data(self):
        """" Test input data set"""
        with self.assertRaises(TypeError) as e:
            get_common_set_data([1, 2, 3], [2, 3, 4])

        self.assertEqual("Input type is not a set", str(e.exception))


class TestSortNamesByAges(unittest.TestCase):
    def test_09_output_type(self):
        """ Test output type"""
        sorted_data = sort_people_by_age(
            [('Alice', 25), ('Boby', 19), ('Charlie', 32),('David', 28), ('Emma', 22), ('Frank', 45)]
        )
        self.assertTrue(isinstance(sorted_data, dict), "Output is not dict")

    def test_10_sorted_names(self):
        """ Test sorted names"""
        sorted_data = sort_people_by_age(
            [('Alice', 25), ('Boby', 19), ('Charlie', 32),('David', 28), ('Emma', 22), ('Frank', 45)]
        )
        self.assertEqual(sorted_data["20-29"], ['Alice', 'David', 'Emma'])
        self.assertEqual(sorted_data["10-19"], ['Boby'])
        self.assertEqual(sorted_data["30-39"], ['Charlie'])
        self.assertEqual(sorted_data["40-49"], ['Frank'])

    def test_11_invalid_age_range(self):
        """ Test invalid age range"""
        with self.assertRaises(ValueError) as e:
            sort_people_by_age([('Frank', 100)])

        self.assertEqual("Values is not in range", str(e.exception))


if __name__ == "__main__":
    unittest.main()
