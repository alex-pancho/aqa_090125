import logging
import pathlib

logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

info_handler = logging.FileHandler("logs/info.log")
info_handler.setLevel(logging.INFO)

error_handler = logging.FileHandler("logs/json_error.log")
error_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(info_handler)
logger.addHandler(error_handler)
logger.addHandler(stream_handler)
