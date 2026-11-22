# Генераторное выражение (в круглых скобках!) — не занимает память
huge_stream = (x * 2 for x in range(10_000_000))
# Вариант 1: Объявить функцию
def process_error(log: str) -> None:
    print(f"Processing error: {log}")




# Функция-генератор с yield
def read_large_log_file(file_path: str):
    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                yield line.strip()  # Возвращает управление вызывающему коду

# Использование
for error_log in read_large_log_file("app.log"):
    process_error(error_log)

