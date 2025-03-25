"""Завдання 1:
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів 
і приберіть їх. Результат запишіть у файл result_<your_second_name>.csv"""

import csv
import json
import logging
import xml.etree.ElementTree as ET
from pathlib import Path

#налаштування логеру
log_file = Path(__file__).parent / "json_samsonkina.log"
logging.basicConfig( 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

#шляхи до CSV файлів
file1_path = Path(__file__).parent / "random.csv"
file2_path = Path(__file__).parent / "random-michaels.csv"

#Функція для зчитування CSV у множину кортежів (унікальні рядки)
def read_csv_file(file_path_js):
    with open(file_path_js, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        return set(tuple(row) for row in reader)

# Зчитуємо дані з обох файлів
data1 = read_csv_file(file1_path)
data2 = read_csv_file(file2_path)

merged_data = data1 | data2

result_file_path = Path(__file__).parent / "result_samsonkina.csv"
with open(result_file_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(merged_data)

print(f"Очищений файл збережено як {result_file_path}")

"""Завдання 2:
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""
json_files = [
    Path(__file__).parent / "localizations_en.json",
    Path(__file__).parent / "localizations_ru.json",
    Path(__file__).parent / "login.json",
    Path(__file__).parent / "swagger.json"
]

def validate_json(file_path_js):
    try:
        with open(file_path_js, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError as e:
        logging.getLogger().handlers[0].setLevel(logging.ERROR)
        logging.error(f"Файл {file_path_js} міcтить помилку JSON: {e}")
        print(f"Файл {file_path_js} невалідний. Деталі записані в лог {log_file}")
    else:
        print(f"Файл {file_path_js} є валідним JSON.")

for json_file in json_files:
    validate_json(json_file)

"""
Завдання 3:
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number 
і повернення значення timingExbytes/incoming результат виведіть у консоль 
через логер на рівні інфо"""

xml_file_path = Path(__file__).parent / "groups.xml"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_timing_exbytes(group_number):
    try:
        logging.getLogger().handlers[1].setLevel(logging.INFO)
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        for group in root.findall("group"):
            number = group.find("number")
            if number is not None and number.text == group_number:
                timing = group.find("timingExbytes/incoming")
                if timing is not None:
                    logging.info(f"Для group/number {group_number}, значення timingExbytes/incoming: {timing.text}")
                    return timing.text
                else:
                    logging.info(f"Для group/number {group_number} не знайдено timingExbytes/incoming")
                    return None
        logging.info(f"Групу з number {group_number} не знайдено")
        return None
    except ET.ParseError as e:
        logging.error(f"Помилка парсингу XML: {e}")
        print(f"Помилка парсингу XML: {e}")

find_timing_exbytes("2")