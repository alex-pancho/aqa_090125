import json
from json import JSONDecodeError
from pathlib import Path

def validate_json(json_files_list):
    for json_file in json_files_list:
        try:
            with open(json_file, 'r', encoding='utf8') as file:
                output_python_dict = json.load(file)
                print(output_python_dict)
        except JSONDecodeError as exc:
            print(exc)

if __name__ == '__main__':
    ext = '.json'
    datasets_dir = Path(__file__).parent / "json_files/"
    list_of_files = [file for file in datasets_dir.iterdir() if file.suffix == ext]
    print(list_of_files)
    validate_json(list_of_files)

