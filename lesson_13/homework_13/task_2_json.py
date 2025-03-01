# main.py
import os
import json
from logger import setup_logger

# Ініціалізація логера
logger = setup_logger()

def validate_json(file_path):
    """Перевірка, чи файл є валідним JSON."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)  # Спроба завантажити вміст як JSON
    except json.JSONDecodeError:
        logger.error(f'Не вдалося зчитати файл {file_path} як JSON')  # Логування помилки
        return False
    except Exception as e:
        logger.error(f'Помилка при зчитуванні файлу {file_path}: {str(e)}')  # Логування іншої помилки
        return False
    return True

def main():
    folder_path = r'C:/Users/HP/Рабочий стол/aqa_090125/lesson_13/homework_13/work_with_json'

    # Перевірка всіх файлів у вказаній папці
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and file_path.endswith('.json'):  # Перевіряємо лише JSON файли
            if not validate_json(file_path):
                logger.error(f"Файл {filename} не є валідним JSON.")  # Записуємо в лог, якщо файл не валідний

if __name__ == '__main__':
    main()
