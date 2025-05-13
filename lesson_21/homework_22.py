from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

Base = declarative_base()
engine = create_engine("sqlite:///students.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Таблиця зв'язку багато-до-багатьох між студентами і курсами
student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=student_course, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship("Student", secondary=student_course, back_populates="courses")

Base.metadata.create_all(engine)

# --- Операції ---
def add_student(name: str, course_ids: list[int]):
    student = Student(name=name)
    session.add(student)  # Додати до сесії до зв'язування з курсами
    for course_id in course_ids:
        course = session.get(Course, course_id)
        if course:
            student.courses.append(course)
    session.commit()

def list_students_on_course(course_title: str):
    course = session.query(Course).filter_by(title=course_title).first()
    if course:
        print(f"Студенти на курсі '{course_title}':")
        for student in course.students:
            print(f"- {student.name}")
    else:
        print("Курс не знайдено.")

def list_courses_for_student(student_name: str):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        print(f"Курси для студента '{student_name}':")
        for course in student.courses:
            print(f"- {course.title}")
    else:
        print("Студента не знайдено.")

def update_student_name(old_name: str, new_name: str):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()
        print("Ім'я оновлено.")
    else:
        print("Студента не знайдено.")

def delete_student(name: str):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()
        print("Студента видалено.")
    else:
        print("Студента не знайдено.")

# --- Демонстрація ---
def seed_data():
    session.query(Student).delete()
    session.query(Course).delete()
    session.commit()

    course_titles = ["Math", "History", "Biology", "Physics", "Art"]
    for title in course_titles:
        session.add(Course(title=title))
    session.commit()

    course_ids = [course.id for course in session.query(Course).all()]
    for i in range(1, 21):
        student_name = f"Student_{i}"
        random_courses = random.sample(course_ids, k=random.randint(1, 3))
        add_student(student_name, random_courses)

if __name__ == "__main__":
    seed_data()
    list_students_on_course("Math")
    list_courses_for_student("Student_1")
    update_student_name("Student_1", "Student_Renamed")
    delete_student("Student_5")