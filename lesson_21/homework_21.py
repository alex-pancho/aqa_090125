from datetime import datetime
from pathlib import Path
import logging

log_folder = Path('D:\\Courses\\Test_homework2\\aqa_090125\\lesson_21')
log_file_path = log_folder / 'hb_test.log'

logging.basicConfig(filename=log_file_path, level=logging.ERROR, 
                    format='%(levelname)s: %(message)s')

def test_heartbeat(log_file, key):
    with open(log_file, 'r') as file:
        lines = file.readlines()
    
    filtered_log = []
    for line in lines:
        if key in line:
            filtered_log.append(line)

    for i in range(len(filtered_log) - 1):
        current_line = filtered_log[i]
        next_line = filtered_log[i + 1]
        
        # шукати першу появу слова "Timestamp " + пропустити довжину слова "Timestamp ", щоб шукати мітку часу
        current_time_search_in_line = current_line.find("Timestamp ") + len("Timestamp ")
        next_time_search_in_line = next_line.find("Timestamp ") + len("Timestamp ")

        # зчитати 8 символів (HH:MM:SS) для отримання часу
        current_time_string = current_line[current_time_search_in_line:current_time_search_in_line + 8]
        next_time_string = next_line[next_time_search_in_line:next_time_search_in_line + 8]

        current_time = datetime.strptime(current_time_string, "%H:%M:%S")
        next_time = datetime.strptime(next_time_string, "%H:%M:%S")

        heartbeat = (current_time - next_time).seconds

        if 31 < heartbeat < 33:
            logging.warning(f'Heartbeat = {heartbeat}sec at {current_time_string} which is >31 and <33')
        elif heartbeat >= 33:
            logging.error(f'Heartbeat = {heartbeat} sec at {current_time_string} which is >=33')

path_to_hblog = Path('D:\\Courses\\Test_homework2\\aqa_090125\\lesson_21\\hblog.txt')
key_to_search = "Key TSTFEED0300|7E3E|0400"
test_heartbeat(path_to_hblog, key_to_search)