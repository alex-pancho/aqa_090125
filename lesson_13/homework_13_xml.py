import xml.etree.ElementTree as ET
from pathlib import Path
from homework_13_json import logging

xml_path = Path(__file__).parent / "groups.xml"

def find_timing_exbytes(file_path, group_number):
    """Функція шукає значення timingExbytes/incoming для заданого group/number у файлі XML."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall("group"):
            if group.findtext("number") == group_number:
                value = group.findtext("timingExbytes/incoming")
                if value:
                    logging.info(f"Знайдене значення: {value}")
                    return value

        logging.info("Значення не знайдено.")
    except Exception as e:
        logging.error(f"Помилка: {e}")

    return None

find_timing_exbytes(xml_path, '5')