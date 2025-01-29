# Заданий список кортежів (ім'я, прізвище, вік, професія, місце проживання): 

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
# 1 - Додайте свій новий запис на початок даного списку. 
new_record = ('Oksana', 'Karnaukh', 31, 'QA Engineer', "Batumi")
people_records.insert(0,new_record)
# 2 - У модифікованому списку обміняйте елементи з індексами 1 і 5 (1<->5). Виведіть результат. 
people_records[1], people_records[5] = people_records[5], people_records[1]
print(people_records)
# 3 - Перевірте, чи всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30.
indexes_check = [6,10,13]
result = all(people_records[i][2] >= 30 for i in indexes_check)
#   Виведіть результат перевірки 
if result == True:
    print(f"Так, всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30")
else:
    print(f"Ні, не всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30")