import unittest
from homework_14_lms import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Іван", "Петренко", 20, 85.5)

    def test_student_creation(self):
        self.assertEqual(str(self.student), "Student: Іван Петренко, age: 20, average grade: 85.50")

    def test_update_grade(self):
        self.student.update_grade(90)
        self.assertEqual(self.student.average_grade, 90)
        self.assertEqual(str(self.student), "Student: Іван Петренко, age: 20, average grade: 90.00")


if __name__ == "__main__":
    unittest.main( verbosity=2)