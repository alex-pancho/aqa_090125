import xml.etree.ElementTree as ET
import logging

# Настройка логирования
log_file = "xml_search_Den.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Файл XML
xml_file = "groups.xml"


def find_timing_exbytes(group_number):
    """Ищет значение timingExbytes/incoming по заданному group/number"""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for group in root.findall(".//group"):
            number = group.find("number")
            if number is not None and number.text == str(group_number):
                timing_exbytes = group.find(".//timingExbytes/incoming")
                if timing_exbytes is not None:
                    result = timing_exbytes.text
                    logging.info(f"Group {group_number} -> incoming: {result}")
                    return result
                else:
                    logging.info(f"Group {group_number} -> incoming не найден")
                    return None

        logging.info(f"Group {group_number} не найден")
        return None

    except ET.ParseError as e:
        logging.error(f"Ошибка парсинга XML: {e}")
        return None
    except FileNotFoundError:
        logging.error(f"Файл {xml_file} не найден")
        return None


# 🔥 Тест поиска
group_to_find = input("Введите номер группы для поиска: ")
result = find_timing_exbytes(group_to_find)

if result:
    print(f"\n✅ Значение incoming для группы {group_to_find}: {result}")
else:
    print(f"\n⚠️ Данные для группы {group_to_find} не найдены или отсутствуют")
1