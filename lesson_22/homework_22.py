from pony.orm import *
import random


db = Database(provider='sqlite', filename='Course.db', create_db=True)

class Student(db.Entity):
    name = Required(str)
    age = Required(int)
    courses = Set('Course')
    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"
    
class Course(db.Entity):
    name = Required(str)
    students = Set(Student)
    def __str__(self):
        return f"Course(name={self.name})"
    def __repr__(self):
        return f"Course(name={self.name})"
    
db.generate_mapping(create_tables=True)


@db_session
def add_student(name:str, age:int):
    return Student(name=name, age=age)
    

@db_session
def add_course(name:str):
    return Course(name=name)
    

@db_session
def add_student_to_course(num_courses_per_student=2):
    students = list(Student.select())  
    courses = list(Course.select())    

    if not courses or not students:
        print("No courses or students available to assign.")
        return

    for student in students:
        student.courses.clear()
        selected_courses = random.sample(courses, min(num_courses_per_student, len(courses)))
        for course in selected_courses:
            student.courses.add(course)


@db_session
def get_students_by_course(course_name: str):
    course = Course.get(name=course_name)
    if course:
        return list(course.students)
    else:
        print(f"Course with name {course_name} not found.")
        return []

@db_session
def get_courses_by_student(student_name: str):
    student = Student.get(name=student_name)
    if student:
        return list(student.courses) 
    else:
        print(f"Student with name {student_name} not found.")
        return []
 

@db_session
def update_student(student_name: str, name: str = None, age: int = None):
    student = Student.get(name=student_name)
    if not student:
        return print(f"Student with name {student_name} not found.")
    if name:
        student.name = name
    if age:
        student.age = age

@db_session
def delete_student(name: str):
    student = Student.get(name=name)
    if student:
        student.delete()
    else:
        print(f"Student with name {name} not found.")


@db_session
def delete_course(name: str):
    course = Course.get(name=name)
    if course:
        course.delete()
    else:
        print(f"Course with name {name} not found.")
   



if __name__ == "__main__":
    with db_session:

        courses = ["Math", "Physics", "Chemistry", "Biology", "History"]
        for course_name in courses:
            add_course(course_name)

        students = [("Alice Jons", 20), ("Bob Talor", 22), ("Charlie Bin", 21), 
                    ("David Bechem", 23), ("Eve Tomas", 19), ("Frank Sinatra", 24),
                    ("Grace Kelly", 22), ("Hank Aaron", 25), ("Ivy League", 21),
                    ("Jack Daniels", 23), ("Kate Winslet", 20), ("Leo Messi", 22),
                    ("Mia Farrow", 21), ("Nina Simone", 23), ("Oscar Wilde", 19),
                    ("Paul Simon", 24), ("Quincy Jones", 22), ("Rita Hayworth", 25),
                    ("Steve Jobs", 21), ("Tina Turner", 23)]
        for name, age in students:
            add_student(name, age)


        add_student_to_course()
        print("Students and their courses:")
        for student in Student.select():
            print(f"{student.name}: {[course.name for course in student.courses]}")


        course = Course.get(name="Math")
        students_in_course = get_students_by_course("Math")
        print(f"Students in {course.name}:")
        for student in students_in_course:
            print(student.name)
    

        student = Student.get(name="Alice Jons")
        courses_of_student = get_courses_by_student("Alice Jons")
        print(f"Courses of {student.name}:")
        for course in courses_of_student:
            print(course.name)
        

        student = Student.get(name="Tina Turner")
        print(f"Student: {student.name}, age: {student.age}")
        update_student(student_name="Tina Turner", name="Tina Tina", age=25)
        student = Student.get(name="Tina Tina")
        print(f"Updated student: {student.name}, age: {student.age}")
        

        delete_student("Bob Talor")
        student = Student.get(name="Bob Talor")
        if student is None:
            print("Student 'Bob Talor' has been deleted.")
        else:
            print(f"Student 'Bob Talor' still exists.")


        delete_course("History")
        course = Course.get(name="History")
        if course is None:
            print("Course 'History' has been deleted.")
        else:
            print(f"Course 'History' still exists.")
