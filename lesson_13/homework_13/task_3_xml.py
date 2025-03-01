import logging
import xml.etree.ElementTree as ET
from pathlib import Path

# Налаштування логера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def find_timing_incoming_by_group_number(xml_file, group_number):
    """Функція для пошуку timingExbytes/incoming за group/number"""
    
    try:
        # Перевірка існування файлу
        xml_path = Path(xml_file)
        if not xml_path.is_file():
            logger.error(f"Файл {xml_file} не знайдено за вказаним шляхом.")
            return None

        # Парсимо XML файл
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Шукаємо групу за number
        for group in root.findall('group'):
            number = group.find('number').text
            if number == str(group_number):
                # Знайшли відповідну групу, тепер шукаємо timingExbytes/incoming
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming').text
                    logger.info(f"Group {group_number} has incoming value: {incoming}")
                    return incoming
                else:
                    logger.warning(f"Group {group_number} does not have 'timingExbytes' or 'incoming'.")
                    return None
        logger.error(f"Group with number {group_number} not found.")
        return None

    except Exception as e:
        logger.error(f"Error processing the XML file: {e}")
        return None

# Виклик функції для тесту
if __name__ == '__main__':
    # Шлях до XML файлу
    xml_file_path = 'C:/Users/HP/Рабочий стол/aqa_090125/lesson_13/homework_13/groups.xml'  # абсолютний шлях
    group_number = 2  # Приклад групи, яку потрібно знайти
    find_timing_incoming_by_group_number(xml_file_path, group_number)
