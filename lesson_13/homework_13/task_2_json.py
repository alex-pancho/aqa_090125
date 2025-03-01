import os
import json
from logger import setup_logger
from pathlib import Path

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
    # Визначаємо шлях до папки work_with_json відносно місця, де знаходиться скрипт
    folder_path = Path(__file__).parent / 'work_with_json'

    # Перевірка всіх файлів у вказаній папці
    for filename in os.listdir(folder_path):
        file_path = folder_path / filename

        if file_path.is_file() and file_path.suffix == '.json':  # Перевіряємо лише JSON файли
            if not validate_json(file_path):
                logger.error(f"Файл {filename} не є валідним JSON.")  # Записуємо в лог, якщо файл не валідний

if __name__ == '__main__':
    main()
