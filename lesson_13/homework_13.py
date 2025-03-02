import csv
import json

import xml.etree.ElementTree as ET
from pathlib import Path

from log import logger


def get_path(file_name):
    return Path(__file__).parent / f"{file_name}"


def read_csv(file_path):
    with open(file_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        data = set(tuple(row) for row in reader)
        return data


def write_csv(file_path, data):
    with open(file_path, 'w', encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def is_valid_json(file):
    try:
        with open(file, 'r', encoding="utf8") as f:
            json.load(f)
            return True
    except json.decoder.JSONDecodeError:
        logger.error(f"{f.name} file is not json")
        return False


def get_xml_incoming_data(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    tag_names = []

    for group in root.findall('group'):
        text = group.find("./timingExbytes/incoming")
        if text is None:
            continue
        logger.info(f"Result text is: {text.text}")
        tag_names.append(text.text)

    return tag_names


if __name__ == '__main__':
    random_file_unique_data = read_csv(get_path("random.csv"))
    rmc_file_unique_data = read_csv(get_path("rmc.csv"))
    unique_data = random_file_unique_data ^ rmc_file_unique_data
    write_csv(get_path("result_csv_path.csv"), unique_data)

    print(is_valid_json(get_path("localizations_en.json")))
    print(is_valid_json(get_path("localizations_ru.json")))
    print(is_valid_json(get_path("login.json")))
    print(is_valid_json(get_path("swagger.json")))

    print(get_xml_incoming_data(get_path("group.xml")))
