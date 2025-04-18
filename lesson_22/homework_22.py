"""
1. Створення моделі даних: 
Створіть просту модель даних для системи управління студентами. Модель може містити таблиці для студентів, курсів та їх відношень.
Кожен студент може бути зареєстрований на декілька курсів. Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.

2. Виконання базових операцій: 
Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
Переконайтеся, що ці зміни коректно відображаються у базі даних.

3. Запити до бази даних: 
Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс, або курси,
на які зареєстрований певний студент.

4. Оновлення та видалення даних: 
Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних.

5. Можна використовувати будь яку ORM на Ваш вібир
"""


import random
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


base = declarative_base()
engine = create_engine("sqlite:///hogwarts.db", echo=False)

student_course = Table(
    'student_course', base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True))

class Student(base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=student_course, back_populates="students")

class Course(base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", secondary=student_course, back_populates="courses")

base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Додавання студента
def add_student(name, course_ids, session=session):
    selected_courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
    new_student = Student(name=name, courses=selected_courses)
    session.add(new_student)
    session.commit()
    print(f"Додан студент {name} на курси: {[c.name for c in selected_courses]}")

# Додавання курсу
def add_course(name, session=session):
    new_course = Course(name=name)
    session.add(new_course)
    session.commit()
    print(f"✅ Додан курс {name}")

# Отримання всіх студентів
def get_all_students(session=session):
    return session.query(Student).all()


def init_data():
    student_names = [
        "Harry Potter", "Hermione Granger", "Ron Weasley",
        "Draco Malfoy", "Neville Longbottom","Luna Lovegood",
        "Ginny Weasley", "Fred Weasley", "George Weasley",
        "Cedric Diggory","Cho Chang", "Seamus Finnigan",
        "Dean Thomas", "Lavender Brown", "Parvati Patil",
        "Padma Patil", "Oliver Wood", "Percy Weasley",
        "Colin Creevey", "Pansy Parkinson"
    ]

    course_names = ["Potions", "Defense Against the Dark Arts", "Transfiguration", "Charms", "Herbology"]

    
    for name in course_names:
        add_course(name)

    all_courses = session.query(Course).all()

    
    for name in student_names:
        selected = random.sample(all_courses, k=random.randint(1, 3))
        new_student = Student(name=name, courses=selected)
        session.add(new_student)

    session.commit()

# Всі студенти і їх курси
def students_and_courses():
    students = get_all_students()
    for student in students:
       if student.courses:
            course_info = ", ".join([f"{course.name} (ID: {course.id})" for course in student.courses])
            print(f"{student.name} (ID: {student.id}) → {course_info}")

# Студенти на курсі
def students_in_course(course_name):
    course = session.query(Course).filter_by(name=course_name).first()
    if course:
        print(f"Студенти курса {course.name}: {[s.name for s in course.students]}")
    else:
        print("Курс не знайдено")

# Курси студента
def courses_of_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        print(f"Курси студента {student.name}: {[c.name for c in student.courses]}")
    else:
        print("Студента не знайдено.")

# Оновлення даних студента
def update_student(student_id, new_name=None, new_course_ids=None, session=session):
    student = session.query(Student).get(student_id)
    if not student:
        print("Студент не знайдено")
        return

    if new_name:
        student.name = new_name
    if new_course_ids is not None:
        student.courses = session.query(Course).filter(Course.id.in_(new_course_ids)).all()

    session.commit()
    print(f"Дані студента оновлено: {student.name}")

# Оновлення даних курсу
def update_course(course_id, new_name=None, session=session):
    course = session.query(Course).get(course_id)
    if not course:
        print("Курс не знайдено")
        return

    if new_name:
        course.name = new_name

    session.commit()
    print(f"Курс оновлено: {course.name}")

# Видалення студента
def delete_student(student_id, session=session):
    student = session.query(Student).get(student_id)
    if not student:
        print("Студент не знайдено")
        return

    session.delete(student)
    session.commit()
    print(f"Студент {student.name} видалений.")
    

if __name__ == "__main__":
    
    if not session.query(Student).first():
        init_data()

    # add_student("Albus Severus Potter", [1, 3])
    # update_student(2, new_course_ids=[1, 2, 3, 4, 5])
    # update_course(2, new_name="Advanced Defense Against the Dark Arts")
    # delete_student(22)

    students_in_course("Potions")

    courses_of_student("Harry Potter")

    print("Всі студенти і їх курси:")
    students_and_courses()