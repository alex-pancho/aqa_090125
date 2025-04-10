import logging
from pathlib import Path
from datetime import datetime

def analyze_log_file(hb_logs_file):
    """
    Analyzes the log file and generates hb_test.log with the results of the heartbeat analysis.
    Uses a logger to record information.
    """

    # Logger
    logging.basicConfig(filename="hb_test.log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    with open(hb_logs_file, "r") as f:
        log_data = f.read()

    filtered_log = []
    for line in log_data.splitlines():
        if "TSTFEED0300|7E3E|0400" in line:
            filtered_log.append(line)

    timestamps = []
    for line in filtered_log:
        timestamp_start = line.find("Timestamp ") + len("Timestamp ")
        timestamp_str = line[timestamp_start:timestamp_start + 8]
        timestamps.append(datetime.strptime(timestamp_str, "%H:%M:%S"))

    for i in range(len(timestamps) - 1):
        heartbeat = (timestamps[i] - timestamps[i + 1]).seconds
        if 31 < heartbeat < 33:
            logging.warning(f"Heartbeat delay: {heartbeat}sec between {timestamps[i+1].strftime('%H:%M:%S')} and {timestamps[i].strftime('%H:%M:%S')}")
        elif heartbeat >= 33:
            logging.error(f"Heartbeat delay: {heartbeat}sec between {timestamps[i+1].strftime('%H:%M:%S')} and {timestamps[i].strftime('%H:%M:%S')}")


if __name__ == '__main__':

    script_dir = Path(__file__).resolve().parent
    hb_logs_file = script_dir / 'hblog.txt'

    analyze_log_file(hb_logs_file)
    