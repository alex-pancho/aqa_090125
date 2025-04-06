import json
import logging
from pathlib import Path

log_file = Path(__file__).parent / "json_Dovhan.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ])

json_file_1 = "localizations_en.json"
with open(json_file_1, 'r', encoding="utf8") as f:
    try:
        content1 = json.load(f)
    except json.decoder.JSONDecodeError as e:
        logging.getLogger().handlers[0].setLevel(logging.ERROR)
        logging.error(f"Файл {json_file_1} міcтить помилку JSON: {e}")
        content2 = f"Файл {json_file_1} не є валідним"


json_file_2 = "login.json"
with open(json_file_2, 'r', encoding="utf8") as f:
    try:
        content2 = json.load(f)
    except json.decoder.JSONDecodeError as e:
        logging.getLogger().handlers[0].setLevel(logging.ERROR)
        logging.error(f"Файл {json_file_2} міcтить помилку JSON: {e}")
        content2 = f"Файл {json_file_2} не є валідним"


json_file_3 = "swagger.json"
with open(json_file_3, 'r', encoding="utf8") as f:
    try:
        content3 = json.load(f)
    except json.decoder.JSONDecodeError as e:
        logging.getLogger().handlers[0].setLevel(logging.ERROR)
        logging.error(f"Файл {json_file_3} міcтить помилку JSON: {e}")
        content3 = f"Файл {json_file_3} не є валідним"

if __name__ == "__main__":
    print(content1)
    print(type(content1))
    print(content2)
    print(type(content2))
    print(content3)
    print(type(content3))