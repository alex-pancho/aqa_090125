import random

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from lesson_22.logger import logger


base = declarative_base()
engine = create_engine("sqlite:///mybase.db", echo=True)

student_course = Table(
    'student_course', base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)


class Student(base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=student_course, back_populates="students")


class Course(base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship("Student", secondary=student_course, back_populates="courses")


class SqlLiteSession:
    def __init__(self):
        self.engine = create_engine("sqlite:///mybase.db", echo=True)
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        base.metadata.create_all(self.engine)

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()

        self.session.close()


def create_students_with_courses():
    with SqlLiteSession() as session:
        course_titles = ['Math', 'Biology', 'History', 'Programming', 'English']
        courses = [Course(title=title) for title in course_titles]
        session.add_all(courses)
        session.commit()

        students = [
            Student(name=f"Student {i}", courses=random.sample(courses, k=random.randint(1, 3)))
            for i in range(1, 21)
        ]

        session.add_all(students)
        session.commit()


def add_new_student_to_course(name, course_name):
    with SqlLiteSession() as session:
        course = session.query(Course).filter_by(title=course_name).first()

        if not course:
            logger.error(f"Course {course_name} not found")
            return

        new_user = Student(name=name, courses=[course])
        session.add(new_user)
        session.commit()


def get_student_info_by_course(course_name):
    with SqlLiteSession() as session:
        course = session.query(Course).filter_by(title=course_name).first()

        if not course:
            logger.error(f"Course {course_name} not found")
            return

        students = []
        for student in course.students:
            students.append(student.name)

        return students


def update_student_info(old_name, new_name):
    with SqlLiteSession() as session:
        student = session.query(Student).filter_by(name=old_name).first()

        if not student:
            logger.error(f"Student {old_name} not found")
            return

        student.name = new_name
        session.commit()


def update_course_title(old_title, new_title):
    with SqlLiteSession() as session:
        course = session.query(Course).filter_by(title=old_title).first()

        if not course:
            logger.error(f"Course {course} not found")
            return

        course.title = new_title
        session.commit()


def delete_student_by_name(name):
    with SqlLiteSession() as session:
        students = session.query(Student).filter_by(name=name).all()

        if not students:
            logger.error(f"Student {name} not found")
            return

        for student in students:
            session.delete(student)
            session.commit()


if __name__ == '__main__':
    create_students_with_courses()
    add_new_student_to_course("Іван Петренко", "Math")
    print(get_student_info_by_course("Math"))
    update_student_info("Іван Петренко", "Іван Макаренко")
    print(get_student_info_by_course("Math"))
    delete_student_by_name("Іван Макаренко")
