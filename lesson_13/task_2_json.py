import json
from json import JSONDecodeError
from pathlib import Path
import logging.config


def validate_json(json_files_list:list=None):
    """ Function receive list of files names/path, validate JSON and write each file result to log """
    if not isinstance(json_files_list, list):
        json_logger.error(f"Function argument must be 'list' type, contains files")
        return

    for json_file in json_files_list:
        try:
            with open(str(json_file), 'r', encoding='utf8') as file:
                output_python_dict = json.load(file)
                json_logger.info(f"{json_file} - OK")
            # Не певен що для перевірки на валідность JSON треба було запис робити
            with open('test_file.json', 'w', encoding='utf8') as file:
                json.dump(output_python_dict, file, indent=4)

        except JSONDecodeError as exc:
            json_logger.error(f"{json_file} - failed, error message={exc}")

        except FileNotFoundError as exc:
            json_logger.error(f"{json_file} - Not found")


logging.config.fileConfig('logger_config.ini')
json_logger = logging.getLogger('json_logger')

if __name__ == '__main__':
    ext = '.json'
    datasets_dir = Path(__file__).parent / "json_files/"
    list_of_files = [file for file in datasets_dir.iterdir() if file.suffix == ext]
    validate_json(list_of_files)
