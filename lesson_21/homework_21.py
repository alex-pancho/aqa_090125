import os
import logging
from datetime import datetime

def analyze_heartbeat_log():
    # Динамічно знаходимо шлях до папки, де лежить сам скрипт
    current_dir = os.path.dirname(__file__)
    
    # Відносний шлях до файлів
    input_file = os.path.join(current_dir, 'hblog.txt')
    output_log = os.path.join(current_dir, 'hb_test.log')

    # Налаштування логування
    logging.basicConfig(
        filename=output_log,
        level=logging.DEBUG,  # Ми можемо писати і WARNING, і ERROR
        format='%(levelname)s: %(message)s',
        filemode='w'  # Щоб перезаписувати файл при кожному запуску
    )

    with open(input_file, 'r') as file:
        lines = file.readlines()

    filtered_log = [line for line in lines if "Key TSTFEED0300|7E3E|0400" in line]

    for i in range(len(filtered_log) - 1):
        # Знаходимо позицію слова 'Timestamp '
        timestamp_pos_1 = filtered_log[i].find('Timestamp ') + len('Timestamp ')
        timestamp_pos_2 = filtered_log[i+1].find('Timestamp ') + len('Timestamp ')

        # Зчитуємо 8 символів для часу
        timestamp_str_1 = filtered_log[i][timestamp_pos_1:timestamp_pos_1 + 8]
        timestamp_str_2 = filtered_log[i+1][timestamp_pos_2:timestamp_pos_2 + 8]

        time1 = datetime.strptime(timestamp_str_1, "%H:%M:%S")
        time2 = datetime.strptime(timestamp_str_2, "%H:%M:%S")

        heartbeat_diff = (time1 - time2).total_seconds()
        if heartbeat_diff < 0:
            heartbeat_diff += 24 * 3600  # на випадок переходу через північ

        if 31 < heartbeat_diff < 33:
            logging.warning(f"Heartbeat {heartbeat_diff} seconds at {timestamp_str_1}")
        elif heartbeat_diff >= 33:
            logging.error(f"Heartbeat {heartbeat_diff} seconds at {timestamp_str_1}")

if __name__ == "__main__":
    analyze_heartbeat_log()
