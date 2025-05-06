"""Завдання 1:

Візміть два файли з теки ideas_for_test/work_with_csv 
порівняйте на наявність дублікатів і приберіть їх. 
Результат запишіть у файл result_<your_second_name>.csv"""

"""Хід роботи:
1. Перевірити наявність дублікатів в одному файлі - прибрати.
2. Перевірити наявність дублікатів в іншому файлі - прибрати.
3. Порівняти два файли на наявність дублікатів і винести дані з них у третій файл."""

import csv
from pathlib import Path
import json
import os
import logging
import xml.etree.ElementTree as ET

# видалити дублікати, залишивши першу появу дублікату у стовпці 'ContactID' з файлу 'random-michaels.csv'
f_csv_path_1 = Path("D:\\Courses\\Hillel IT School\\QA Automation Python\\HW_QA Python\\lessons\\les_13_hw\\random-michaels.csv")
income_file_michaels = f_csv_path_1
path_to_les_13_hw = Path("D:\\Courses\\Hillel IT School\\QA Automation Python\\HW_QA Python\\lessons\\les_13_hw")
file_michaels_without_duplicates = path_to_les_13_hw / "random_michaels_updated.csv"

records_in_file_michaels = set()
original_rows_in_file_michaels = []

with open(f_csv_path_1, 'r', encoding='utf8') as f:
    reader_michaels = csv.DictReader(f) # DictReader використовується для доступу за назвою стовпця
    name_of_title = reader_michaels.fieldnames # отримуємо заголовки стовпців

    for row in reader_michaels:
        user_id = row["ContactID".strip()] # вказуємо назву стовпця, за яким буде відбуватися пошук

        if user_id not in records_in_file_michaels:
            records_in_file_michaels.add(user_id)
            original_rows_in_file_michaels.append(row)

# записати зміни у новий файл
with open (file_michaels_without_duplicates, 'w', encoding='utf8', newline="") as f:
    write_changes = csv.DictWriter(f, fieldnames=name_of_title)
    write_changes.writeheader()  # Записуємо заголовки
    write_changes.writerows(original_rows_in_file_michaels)  # Записуємо очищені дані

# видалити дублікати, залишивши першу появу дублікату у стовпці 'ContactID' з файлу 'random.csv'
f_csv_path_2 = Path("D:\\Courses\\Hillel IT School\\QA Automation Python\\HW_QA Python\\lessons\\les_13_hw\\random.csv")
income_file_random = f_csv_path_2
file_michaels_without_duplicates = path_to_les_13_hw / "random_updated.csv"

records_in_file_random = set()
original_rows_in_file_random = []

with open(f_csv_path_1, 'r', encoding='utf8') as f:
    reader_michaels = csv.DictReader(f) # DictReader використовується для доступу за назвою стовпця
    name_of_title = reader_michaels.fieldnames # отримуємо заголовки стовпців

    for row in reader_michaels:
        user_id = row["ContactID".strip()] # назва стовпця, за яким буде відбуватися пошук

        if user_id not in records_in_file_random:
            records_in_file_random.add(user_id)
            original_rows_in_file_random.append(row)

# записати зміни у новий файл
with open (file_michaels_without_duplicates, 'w', encoding='utf8', newline="") as f:
    write_changes = csv.DictWriter(f, fieldnames=name_of_title)
    write_changes.writeheader()  # Записуємо заголовки
    write_changes.writerows(original_rows_in_file_random)  # Записуємо очищені дані

random_michaels_updated_path = Path("D:\\Courses\\Hillel IT School\\QA Automation Python\\HW_QA Python\\lessons\\les_13_hw\\random_michaels_updated.csv")
random_updated_path = Path("D:\\Courses\\Hillel IT School\\QA Automation Python\\HW_QA Python\\lessons\\les_13_hw\\random_updated.csv")
merged_files_without_duplicates = path_to_les_13_hw / "result_Synelnykova.csv"

# Читаємо перший файл
data_from_file = {}

with open(random_michaels_updated_path, 'r', encoding='utf8') as f:
    reader_f1 = csv.DictReader(f)
    get_fieldnames = reader_f1.fieldnames  # Отримуємо заголовки
    for row in reader_f1:
        data_from_file[row["ContactID"].strip()] = row  # Зберігаємо унікальні ID

# Читаємо другий файл
with open(random_updated_path, 'r', encoding='utf8') as f:
    reader_f2 = csv.DictReader(f)
    for row in reader_f2:
        data_from_file[row["ContactID"].strip()] = row

# Результати записюємо у новий CSV-файл
with open(merged_files_without_duplicates, 'w',  newline='', encoding='utf8',) as f:
    write_changes = csv.DictWriter(f, fieldnames=get_fieldnames)
    write_changes.writeheader()
    write_changes.writerows(data_from_file.values())


"""Завдання 2:

Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log"""

path_to_dir = Path("D://Courses//Hillel IT School//QA Automation Python//HW_QA Python//lessons//les_13_hw//work_with_json")

logging.basicConfig(filename='log_json.log', 
                    level=logging.ERROR, encoding="utf8", 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def valid_or_no(dir):
    """Validates if file have an '.json' extension and if it is a valid json file"""
    valid_json = []
    invalid_file = []
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)

        if file.lower().endswith(".json"):
            try:
                with open(file_path,'r', encoding='utf8') as f:
                    json.load(f)
                valid_json.append(file)
            except json.JSONDecodeError:
                logging.error(f'Файл {file_path} не валідний')

    if valid_json:
        return f'Валідні json файли: {len(valid_json)}, {valid_json}'
    if invalid_file:
        return f'Невалідні файли: {len(invalid_file)}, {invalid_file}'

check = valid_or_no(path_to_dir)
print(check)


"""Завдання 3:

Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number 
і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо"""

file_groups_path = Path("D://Courses//Hillel IT School//QA Automation Python//HW_QA Python//lessons//les_13_hw//work_with_xml//groups.xml")
logging.basicConfig(filename='log_xml.log', 
                    level=logging.INFO, encoding="utf8", 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def find_incoming_value(xml_path, search_number):
    """Function for search by group/number in xml file"""
    try:
        tree = ET.parse(xml_path) #  зчитує XML-файл і перетворює його в дерево
        root = tree.getroot() # отримуємо кореневий елемент дерева

        for group in root.findall("group"):
            number = group.find("number")
            if number is not None and number.text == str(search_number):
                # Шукаємо тег <timingExbytes> -> <incoming>
                timing_exbytes = group.find("timingExbytes")
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find("incoming")
                    if incoming is not None:
                        logging.info(f"Значення 'incoming' для групи {search_number}: {incoming.text}")
                        return incoming.text

    except ET.ParseError as e:
        logging.error(f"Помилка ParseError: {e}")
        return None


xml_file_path = file_groups_path 
group_number = 2

find_incoming_value(xml_file_path, group_number)

