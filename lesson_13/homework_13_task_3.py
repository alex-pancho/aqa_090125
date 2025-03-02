# Завдання 3:
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію 
# пошуку по group/number і повернення значення timingExbytes/incoming 
# результат виведіть у консоль через логер на рівні інфо

import xml.etree.ElementTree as ET
import logging
from pathlib import Path

def find_incoming_by_group_number(xml_file, group_number):
    #Logger
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall('group'):
        number_element = group.find('number')
        if number_element is not None and int(number_element.text) == group_number:
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming_element = timing_exbytes.find('incoming')
                if incoming_element is not None:
                    logging.info(f"timingExbytes/incoming for group {group_number} is: {incoming_element.text}")
                    return incoming_element.text
            else:
                logging.info(f"No data for group {group_number}.")    
    return None

xml_file = Path(__file__).parent / "groups.xml"

find_incoming_by_group_number(xml_file, 2)
find_incoming_by_group_number(xml_file, 1)
