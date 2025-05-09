from datetime import datetime, timedelta
from pathlib import Path

from lesson_21.logger import logger

DIR_PATH = Path(__file__).parent / 'hblog.txt'
TARGET_KEY = 'Key TSTFEED0300|7E3E|0400'


def get_log(path):
    with open(path, 'r', encoding='utf') as f:
        lines = f.readlines()
        for line in lines:
            yield line


def analyze_heartbeat(path, target_key):
    logs = get_log(path)
    timestamps = []

    data_log = [log for log in logs if target_key in log]

    for log in data_log:
        pos = log.find("Timestamp ")
        if pos != -1:
            timestamp = log[pos + len("Timestamp "):pos + len("Timestamp ") + 8]
            timestamps.append(datetime.strptime(timestamp, '%H:%M:%S'))

    for i in range(len(timestamps) - 1):
        current_time = timestamps[i]
        next_time = timestamps[i + 1]
        diff = current_time - next_time

        if timedelta(seconds=31) < diff < timedelta(seconds=33):
            logger.warning(f"Heartbeat delay: {diff} seconds between {current_time.time()} and {next_time.time()}")
        elif diff >= timedelta(seconds=33):
            logger.error(f"Heartbeat delay: {diff} seconds between {current_time.time()} and {next_time.time()}")


if __name__ == '__main__':
    analyze_heartbeat(DIR_PATH, TARGET_KEY)
