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

def find_timing_incoming_by_group_number(group_number):
    """Функція для пошуку timingExbytes/incoming за group/number"""
    try:
        # Визначаємо шлях до XML файлу відносно місця, де знаходиться скрипт
        xml_path = Path(__file__).parent / 'groups.xml'
        
        # Перевірка існування файлу
        if not xml_path.is_file():
            logger.error(f"Файл {xml_path} не знайдено.")
            return None

        # Парсимо XML файл
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # Шукаємо групу за number
        for group in root.findall('group'):
            number = group.find('number').text
            if number == str(group_number):
                # Знайшли відповідну групу, тепер шукаємо timingExbytes/incoming
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming').text
                    logger.info(f"Group {group_number} має значення incoming: {incoming}")
                    return incoming
                else:
                    logger.warning(f"Group {group_number} не має 'timingExbytes' або 'incoming'.")
                    return None
        logger.error(f"Групу з номером {group_number} не знайдено.")
        return None

    except Exception as e:
        logger.error(f"Помилка при обробці XML файлу: {e}")
        return None

# Виклик функції для тесту
if __name__ == '__main__':
    group_number = 2  # Приклад групи, яку потрібно знайти
    find_timing_incoming_by_group_number(group_number)
