import logging

def configure_logging():
    logging.basicConfig(
        filename="logs/test_log.txt",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )