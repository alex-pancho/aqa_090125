"""Створення моделі даних: 
-> Створіть просту модель даних для системи управління студентами. 
Модель може містити таблиці для студентів, курсів та їх відношень. 
Кожен студент може бути зареєстрований на декілька курсів. 
- Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.

Виконання базових операцій:
-> Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
Переконайтеся, що ці зміни коректно відображаються у базі даних.

Запити до бази даних:
-> Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних.
Можна використовувати будь яку ORM на Ваш вибір"""

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

base = declarative_base()
engine = create_engine("sqlite:///hw_22.db", echo=True)
    
class Courses(base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    student = relationship("Student", back_populates="course")

class Student(base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    student_name = Column(String)
    student_surname = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship("Courses", back_populates="student")

base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_new_student_to_students(name='Vasyl', surname='Stepko', course_name = 'FIT 1-5f', session=session):
    """Add new student and relative course to table Student"""
    course = session.query(Courses).filter_by(course_name=course_name).first()
    if not course:
        course = Courses(course_name=course_name)
        session.add(course)
        session.commit()

    new_student = Student(student_name=name, student_surname=surname, course_id = course.id)
    session.add(new_student)
    session.commit()
    return new_student
    
def delete_user(student_id, session=session):
    """Delete student and his/her courses"""
    student = session.query(Student).filter_by(id=student_id).first()

    if student:
        session.delete(student)
        session.commit()

        print(f'Видалено студента з ID {student_id}')
    else:
        print(f'Не знайдено студента з ID {student_id}')

#1
add_new_student_to_students('Vasyl', 'Stepko', 'FIT 1-5f')
# #2
add_new_student_to_students('Diana', 'Korolenko', 'FIOT 3d')
# #3
add_new_student_to_students('Martyn', 'Novak', 'IEE 2024')
#4
add_new_student_to_students('Maria', 'Krushelnytska', 'FIOT 3d')
#5
add_new_student_to_students('Petro', 'Davudyv', 'FIT 1-5f')
# #6
add_new_student_to_students('Natalia', 'Shpak', 'FIOT 3d')
#7
add_new_student_to_students('Alex', 'Lun', 'FIT 1-5f')
#8
add_new_student_to_students('Fedir', 'Revutskyi', 'FIOT 3d')
#9
add_new_student_to_students('Vitalina', 'Ivashchenko', 'IEE 2024')
#10
add_new_student_to_students('Nadia', 'Prokuda', 'IPSA 4b')
#11
add_new_student_to_students('Nestor', 'Pidbyvajlo', 'IEE 2024')
#12
add_new_student_to_students('Ivan', 'Radchenko', 'IPSA 4b')
#13
add_new_student_to_students('Dmytro', 'Dub', 'IEE 2024')
#14
add_new_student_to_students('Ivanna', 'Oprushko', 'IPSA 4b')
#15
add_new_student_to_students('Hanna', 'Buzna', 'IEE 2024')
#16
add_new_student_to_students('Olha', 'Skrypka', 'IPSA 4b')
#17
add_new_student_to_students('Volodymyr', 'Kit', 'EF 4-2k')
#18
add_new_student_to_students('Stepan', 'Zhurytskty', 'EF 4-2k')
#19
add_new_student_to_students('Nella', 'Ostapenko', 'EF 4-2k')
#20
add_new_student_to_students('Mykola', 'Lapunko', 'EF 4-2k')

def select_all_students():
    """Equal SELECT * FROM students"""
    all_students = session.query(Student).all()
    return all_students

def student_course(all_students:list):
    """Search relative course to all students"""
    for student in all_students:
        course = session.query(Courses).filter_by(id=student.course_id).first()
        course_name = course.course_name
        print(f'Student Data -> Student name: {student.student_name}, student surname: {student.student_surname}, student course: {course_name}')

if __name__ == "__main__":
    all_users = select_all_students()
    student_course(all_users)
    delete_user(1)


