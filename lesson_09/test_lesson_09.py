import unittest

def is_sub_string_find(sub_string:str, string:str) -> bool:
    """ Function to find a substring in a string """
    return string.find(sub_string) != -1

class TestSubStringFind(unittest.TestCase):

    def test_01_sub_string_find_positive(self):
        """ Test for positive cases: substring is found in the string """
        self.assertTrue(is_sub_string_find("abc", "abcdef"))
        self.assertEqual(is_sub_string_find("b", "abcdef"), True)

    def test_02_sub_string_find_negative(self):
        """ Test for negative cases: substring is not found in the string """
        self.assertEqual(is_sub_string_find("abc", "def"), False)
        self.assertEqual(is_sub_string_find("abc", "ABCDEF"), False)
    
    def test_03_sub_string_find_in_ar(self):
        actual_result = "Test for negative cases: substring is not found in the string 342387643872"
        expected_result = "Test for negative cases: substring is not found in the string"
        self.assertIn(expected_result, actual_result, msg=f"Substring {expected_result} not found in the string")

if __name__ == "__main__":
    unittest.main(verbosity=2)
    # print(sub_string_find("abc", "abcdef")) # True
    # print(sub_string_find("abc", "def")) # False
    # print(sub_string_find("abc", "ABCDEF")) # False