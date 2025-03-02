from pathlib import Path 
import csv
import json
import xml.etree.ElementTree as ET
import logging

# Завдання 1:
# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх. 
# Результат запишіть у файл result_<your_second_name>.csv

def remove_duplicates(file_1: Path, file_2: Path, output_path: Path) -> None:
    """
    Remove duplicates from two csv files and write the result to a new csv file.
    file_1: Path to the first csv file
    file_2: Path to the second csv file
    output_path: Path to the output
    """

    with open(file_1, 'r') as file:
        reader = csv.reader(file)
        set_1 = set(tuple(row) for row in reader)

    with open(file_2, 'r') as file:
        reader = csv.reader(file)
        set_2 = set(tuple(row) for row in reader)

    set_3 = set_1.union(set_2)

    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(set_3)

csv_1 = Path("/Users/kate/Documents/Курсы/aqa_090125/lesson_13/homework_13/csv_files/random-michaels.csv")
csv_2 = Path("/Users/kate/Documents/Курсы/aqa_090125/lesson_13/homework_13/csv_files/random.csv")
output_path = Path("/Users/kate/Documents/Курсы/aqa_090125/lesson_13/homework_13/result_kate.csv")
remove_duplicates(csv_1, csv_2, output_path) 


# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
# Результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

def validate_json_files(*files: Path, log_path: Path) -> None:
    """
    Validate json files.
    files: Paths to json files
    log_path: Path to the log file
    """

    logging.basicConfig(
        filename=log_path,
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
        )
    logger = logging.getLogger("json")

    for file in files:
        try:
            with open(file, 'r') as f:
                json.load(f)
        except json.JSONDecodeError:
            logger.error(f"File {file.name} is not a valid json file") 

json_1 = Path("/Users/kate/Documents/Курсы/aqa_090125/lesson_13/homework_13/json_files/localizations_en.json")
json_2 = Path("/Users/kate/Documents/Курсы/aqa_090125/lesson_13/homework_13/json_files/localizations_ru.json")
json_3 = Path("/Users/kate/Documents/Курсы/aqa_090125/lesson_13/homework_13/json_files/login.json")
json_4 = Path("/Users/kate/Documents/Курсы/aqa_090125/lesson_13/homework_13/json_files/swagger.json")
log_path = Path("/Users/kate/Documents/Курсы/aqa_090125/lesson_13/homework_13/json_kate.log")
validate_json_files(json_1, json_2, json_3, json_4, log_path=log_path)


# Завдання 3:
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і 
# повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо   

def find_group_by_number(xml_path: Path) -> None:
    """
    Find group by number and return the value of timingExbytes/incoming.
    xml_path: Path to the xml file
    """

    tree = ET.parse(xml_path)
    root = tree.getroot()

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("xml")

    for group in root.findall('group'):
        number = group.find('number').text
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming').text
            logger.info(f"Group number: {number}, incoming: {incoming}")

xml_path = Path("/Users/kate/Documents/Курсы/aqa_090125/lesson_13/homework_13/xml_files/groups.xml") 
find_group_by_number(xml_path)


