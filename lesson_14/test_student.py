import pytest
from homework_14_lms import Student

def test_student_initialization():
    student = Student("Rose", "Tyler", 20, 4.5)
    assert student.first_name == "Rose"
    assert student.last_name == "Tyler"
    assert student.age == 20
    assert student.avg_score == 4.5

def test_update_average_score_positive():
    student = Student("Amelia", "Pond", 22, 4.0)
    student.update_average_score(4.8)
    assert student.avg_score == 4.8

def test_update_average_score_zero():
    student = Student("John", "Show", 21, 3.5)
    student.update_average_score(0.0)
    assert student.avg_score == 0.0

def test_update_average_score_negative():
    student = Student("Osvin", "Osvald", 19, 4.2)
    student.update_average_score(-1.0)
    assert student.avg_score == -1.0