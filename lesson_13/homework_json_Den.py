import os
import json
import logging

# Настройка логирования
log_file = "json_validation_Den.log"
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Папка с JSON-файлами (абсолютный путь, если файлы не находятся)
json_folder = r"C:\Users\cdo\Desktop\Hillel\autotesting_by_python\aqa_local_repo\aqa_090125\lesson_13"

# Получаем список всех JSON-файлов в папке
json_files = [f for f in os.listdir(json_folder) if f.endswith(".json")]

# Проверяем, есть ли вообще файлы
if not json_files:
    print("⚠️ В указанной папке нет JSON-файлов! Проверь путь.")
    exit(1)

# Проверяем файлы
invalid_files = []

print(f"\n📂 Найдено JSON-файлов: {len(json_files)}")

for file in json_files:
    file_path = os.path.join(json_folder, file)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json.load(f)  # Попытка загрузить JSON
        print(f"✅ {file} - валидный JSON")
    except json.JSONDecodeError as e:
        error_message = f"❌ {file} - НЕВАЛИДНЫЙ JSON! Ошибка: {e}"
        print(error_message)
        logging.error(error_message)
        invalid_files.append(file)

# Итоговый вывод
if invalid_files:
    print("\n⚠️ Найдены невалидные JSON-файлы! Ошибки записаны в лог.")
else:
    print("\n🎯 Все файлы валидны!")

print(f"\n📜 Лог ошибок сохранен в: {log_file}")
