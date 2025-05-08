import logging

# Створення логера
logger = logging.getLogger(__name__)

# Налаштування рівня логування
base_log_level = logging.INFO

logger.setLevel(base_log_level)

# Створення обробника для виводу в stdout (консоль)
console_handler = logging.StreamHandler()

# Створення обробника для запису в файл
file_handler = logging.FileHandler('logfile.txt')

# Налаштування рівня логування для обробників
console_handler.setLevel(base_log_level)
file_handler.setLevel(base_log_level)

# Створення форматера для обробників
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Налаштування форматера для обробників
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Додавання обробників до логера
logger.addHandler(console_handler)
logger.addHandler(file_handler)
