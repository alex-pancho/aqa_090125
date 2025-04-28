from pony.orm import *

db = Database()

class Student(db.Entity):
    name = Required(str)
    email = Required(str, unique=True)
    enrollments = Set("Enrollment")

class Course(db.Entity):
    name = Required(str)
    teacher = Required(str)
    enrollments = Set("Enrollment")

class Enrollment(db.Entity):
    student = Required(Student)
    course = Required(Course)

db.bind(provider='sqlite', filename='students.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


@db_session
def add_student(name, email, course_name):
    course = Course.get(name=course_name)
    if not course:
        print(f"Course '{course_name}' not found.")
        return
    student = Student(name=name, email=email)
    Enrollment(student=student, course=course)
    print(f"Added {name} ({email}) to {course_name}.")


@db_session
def get_students_in_course(course_name):
    course = Course.get(name=course_name)
    if course:
        print(f"Students in {course_name}:")
        for e in course.enrollments:
            print(f"- {e.student.name} ({e.student.email})")
    else:
        print(f"Course '{course_name}' not found.")


@db_session
def get_courses_for_student(student_name):
    student = Student.get(name=student_name)
    if student:
        print(f"Courses for {student.name} ({student.email}):")
        for e in student.enrollments:
            print(f"- {e.course.name} (Teacher: {e.course.teacher})")
    else:
        print(f"Student '{student_name}' not found.")


@db_session
def update_student_name(old_name, new_name):
    student = Student.get(name=old_name)
    if student:
        student.name = new_name
        print(f"Updated student name from {old_name} to {new_name}.")
    else:
        print(f"Student '{old_name}' not found.")


@db_session
def delete_student(name):
    student = Student.get(name=name)
    if student:
        student.delete()
        print(f"Deleted student '{name}'.")
    else:
        print(f"Student '{name}' not found.")



if __name__ == "__main__":

    with db_session:
        course_data = [
            ("Mathematics", "Dr. Alan Turing"),
            ("Physics", "Dr. Marie Curie"),
            ("History", "Prof. Yuval Harari"),
            ("Biology", "Dr. Jane Goodall"),
            ("Computer Science", "Dr. Donald Knuth")
        ]
        course_objs = {}
        for name, teacher in course_data:
            course_objs[name] = Course(name=name, teacher=teacher)

        student_data = [
            ("Alice Smith", "alice@example.com"),
            ("Bob Johnson", "bob@example.com"),
            ("Charlie Brown", "charlie@example.com"),
            ("Diana Prince", "diana@example.com"),
            ("Evan Miller", "evan@example.com"),
            ("Fiona Davis", "fiona@example.com"),
            ("George Wilson", "george@example.com"),
            ("Hannah Clark", "hannah@example.com"),
            ("Ivan Moore", "ivan@example.com"),
            ("Julia Adams", "julia@example.com"),
            ("Kevin Lee", "kevin@example.com"),
            ("Laura Scott", "laura@example.com"),
            ("Mike Taylor", "mike@example.com"),
            ("Nina Roberts", "nina@example.com"),
            ("Oscar White", "oscar@example.com"),
            ("Paula Turner", "paula@example.com"),
            ("Quinn Hall", "quinn@example.com"),
            ("Rachel Young", "rachel@example.com"),
            ("Sam Green", "sam@example.com"),
            ("Tina Baker", "tina@example.com")
        ]
        student_objs = []
        for name, email in student_data:
            student_objs.append(Student(name=name, email=email))


        enrollments = [
            (0, "Mathematics"), (1, "Mathematics"), (2, "Mathematics"), (3, "Mathematics"),
            (4, "Physics"), (5, "Physics"), (6, "Physics"), (7, "Physics"),
            (8, "History"), (9, "History"), (10, "History"), (11, "History"),
            (12, "Biology"), (13, "Biology"), (14, "Biology"), (15, "Biology"),
            (16, "Computer Science"), (17, "Computer Science"), (18, "Computer Science"), (19, "Computer Science")
        ]

        for student_index, course_name in enrollments:
            Enrollment(student=student_objs[student_index], course=course_objs[course_name])

    add_student("Zoe Parker", "zoe@example.com", "Biology")
    get_students_in_course("Biology")
    get_courses_for_student("Zoe Parker")
    update_student_name("Zoe Parker", "Zoe P.")
    get_courses_for_student("Zoe P.")
    delete_student("Zoe P.")
    get_students_in_course("Biology")
