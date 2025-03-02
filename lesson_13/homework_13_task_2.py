# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. 
# Pезультат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

import os
import json
import logging
from pathlib import Path

def validate_json_files(folder_path, log_file):
    # Logger
    logging.basicConfig(filename=log_file, level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Check file in folder if it is valid json
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                logging.error(f"File {filename} is not valid: {e}")

json_folder_path = Path(__file__).parent / 'work_with_json'
log_file = "json__lesyk.log"

validate_json_files(json_folder_path, log_file)