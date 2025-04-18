from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

BaseClass = declarative_base()

class Student(BaseClass):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Course(BaseClass):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)

student_course = Table(
    'student_course', BaseClass.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

Student.courses = relationship("Course", secondary=student_course, back_populates="students")
Course.students = relationship("Student", secondary=student_course, back_populates="courses")

# створення БД і сесії
engine = create_engine('sqlite:///students.db')
BaseClass.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#додаємо курси
course_names = [
    "Python Programming",
    "Web Development with JavaScript",
    "Databases and SQL",
    "Software Testing",
    "Algorithms and Data Structures"
]
courses = [Course(name=name) for name in course_names]
session.add_all(courses)
session.commit()

#додаємо студентів
students = []
for i in range(1, 21):
    student = Student(name=f"Student {i}", email=f"student{i}@gmail.com")
    student.courses = random.sample(courses, k=random.randint(1, 3))
    students.append(student)

session.add_all(students)
session.commit()

# CRUD-клас
class StudentManager:
    def __init__(self, session):
        self.session = session

    def add_student_to_course(self, name, email, course_id):
        course = self.session.query(Course).filter_by(id=course_id).first()
        if course:
            student = Student(name=name, email=email)
            student.courses.append(course)
            self.session.add(student)
            self.session.commit()
            print(f"Student '{name}' has been added to course '{course.name}'")
        else:
            print("Course not found.")

    def get_students_in_course(self, course_id):
        course = self.session.query(Course).filter_by(id=course_id).first()
        if course:
            return [student.name for student in course.students]
        return []
    
    def get_courses_for_student(self, student_id):
        student = self.session.query(Student).filter_by(id=student_id).first()
        if student:
            return [course.name for course in student.courses]
        return []
    
    def update_student_name(self, student_id, new_name):
        student = self.session.query(Student).filter_by(id=student_id).first()
        if student:
            student.name = new_name
            self.session.commit()
            print(f"Student name with ID {student_id} has been updated to '{new_name}'")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        student = self.session.query(Student).filter_by(id=student_id).first()
        if student:
            self.session.delete(student)
            self.session.commit()
            print(f"Student with ID {student_id} has been deleted.")
        else:
            print("Student not found")

# Приклад використання
if __name__ == "__main__":

    manager = StudentManager(session)
    
    manager.add_student_to_course("Svitlana", "svit1234@gmail.com", 1)
    print(manager.get_students_in_course(1))
    print(manager.get_courses_for_student(6))
    manager.update_student_name(20, "Lana")
    manager.delete_student(20)


