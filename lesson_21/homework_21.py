from datetime import datetime
import re
import logging
from pathlib import Path

# Налаштування логера
def setup_logger(output_file):
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(asctime)s | %(message)s',
        datefmt='%H:%M:%S',
        handlers=[
            logging.FileHandler(output_file),
            logging.StreamHandler()
        ]
    )

def read_and_filter_lines(input_file, key):
    """"Читає лог-файл та фільтрує рядки за ключем."""
    path = Path(input_file)
    if not path.exists():
        logging.error(f"File is not found: {input_file}")
        return []
    with path.open('r', encoding='utf-8') as f:
        return [line for line in f if key in line]

def extract_timestamps(filtered_lines):
    """Витягує мітки часу з фільтрованих рядків."""
    timestamps = []
    for line in filtered_lines:
        match = re.search(r"Timestamp (\d{2}:\d{2}:\d{2})", line)
        if match:
            time_str = match.group(1)
            try:
                time_obj = datetime.strptime(time_str, "%H:%M:%S")
                timestamps.append((time_obj, time_str))
            except ValueError:
                continue
    return timestamps

def analyze_time_differences(timestamps):
    """Аналізує різницю між мітками часу та логує попередження або помилки."""
    for i in range(len(timestamps) - 1):
        t_prev, s_prev = timestamps[i]
        t_next, s_next = timestamps[i + 1]
        delta = int((t_next - t_prev).total_seconds())
        if delta < 0:
            delta += 86400

        delta_int = int(delta)
        if 31 < delta < 33:
            logging.warning(f"Heartbeat delay: {delta_int}sec between {s_prev} and {s_next}")
        elif delta >= 33:
             logging.error(f"Heartbeat delay: {delta_int}sec between {s_prev} and {s_next}")
    

def analyze_heartbeat_log(input_file, output_file, key):
    """Основна функція, що керує процесом аналізу логів heartbeat."""
    setup_logger(output_file)
    filtered_lines = read_and_filter_lines(input_file, key)
    if not filtered_lines:
        return
    timestamps = extract_timestamps(filtered_lines)
    timestamps.sort(key=lambda x: x[0])
    analyze_time_differences(timestamps)
    
if __name__ == "__main__":
    analyze_heartbeat_log(
        input_file="lesson_21/hblog.txt",
        output_file="hb_test.log",
        key="TSTFEED0300|7E3E|0400"
    )