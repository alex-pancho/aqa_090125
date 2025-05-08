from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


base = declarative_base()
engine = create_engine("sqlite:///mybase.db", echo=True) 
# "sqlite://" - база створюється в пам'яті

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class Department(base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("Employee", back_populates="department")

class Employee(base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))
    # Встановлення відношення "багато до одного" з таблицею Department
    department = relationship("Department", back_populates="employees")

base.metadata.create_all(engine)

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()
# Додавання нового користувача
def add_new_item_to_user(name='Andrey', age=30, session=session):
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
# add_new_item_to_user("Petro", 25)

def select_all_user():
    all_users = session.query(User).all()
    return all_users

def filtered_by(**kwargs):
    return session.query(User).filter_by(**kwargs)

def out_users_data(all_users:list):
    for user in all_users:
        print(user.age, user.name, user.id)

# it_department = Department(name='IT')
# hr_department = Department(name='HR')

# john = Employee(name='John', department=it_department)
# alice = Employee(name='Alice', department=hr_department)
# bob = Employee(name='Bob', department=it_department)

# session.add_all([it_department, hr_department, john, alice, bob])
# session.commit()

if __name__ == "__main__":
    all_users = select_all_user()
    out_users_data(all_users)

    johns = filtered_by(name='John') #session.query(User).filter_by()
    out_users_data(johns)

    average_age = session.query(func.avg(User.age)).scalar()
    print("Середній вік користувачів:", average_age)

    user_count = session.query(func.count(User.id)).scalar()
    print("Кількість користувачів:", user_count)

    employees = session.query(Employee).all()
    for employee in employees:
        print(f"Ім'я: {employee.name}, Департамент: {employee.department.name}")
    
