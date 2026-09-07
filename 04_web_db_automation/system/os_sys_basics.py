import sys
import os


if len(sys.argv) < 2:
    print("Ошибка: Передайте имя датчика. Пример: python main.py TEMP_1")
    sys.exit(1)

sensor_name = sys.argv[1]
print(f"Работаем с датчиком: {sensor_name}")


db_password = os.environ.get("DB_PASSWORD", "default_dev_pass")
log_path = os.path.join("logs", "greenhouse.log")

if os.path.exists(log_path):
    print(f"Файл логов найден, его размер: {os.path.path.getsize(log_path)} байт")