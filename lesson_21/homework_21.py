from datetime import datetime, timedelta
from pathlib import Path
import logging


def parse_log_file(file_path: Path):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    filtered_log = []
    for line in lines:
        if "Key TSTFEED0300|7E3E|0400" in line:
            filtered_log.append(line)

    return filtered_log


def analyze_heartbeat(log_lines):

    logging.basicConfig(
        filename='/Users/kate/Documents/Курсы/aqa_090125/lesson_21/hb_test.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    timestamps = []
    for line in log_lines:
        start_index = line.find("Timestamp ")
        if start_index != -1:
            timestamp_str = line[start_index + 10:start_index + 18]
            timestamps.append(datetime.strptime(timestamp_str, "%H:%M:%S"))

    for i in range(len(timestamps) - 1):
        time_diff = timestamps[i] - timestamps[i+1]

        if timedelta(seconds=31) < time_diff < timedelta(seconds=33):
            logging.warning(f"Heartbeat warning: {time_diff} seconds at {timestamps[i].strftime('%H:%M:%S')}")
        elif time_diff >= timedelta(seconds=33):
            logging.error(f"Heartbeat error: {time_diff} seconds at {timestamps[i].strftime('%H:%M:%S')}")
        
        
    

if __name__ == "__main__":
    log_file_path = Path("/Users/kate/Documents/Курсы/aqa_090125/lesson_21/hblog.txt")
    log_lines = parse_log_file(log_file_path)
    analyze_heartbeat(log_lines)