import argparse

def main():
    # 1. Создаем парсер с описанием утилиты
    parser = argparse.ArgumentParser(description="Greenhouse CLI Tool (Argparse)")

    # 2. Добавляем обязательный позиционный аргумент
    parser.add_argument("sensor_id", type=str, help="ID датчика (например, TEMP_1)")

    # 3. Добавляем необязательный флаг с дефолтным значением
    parser.add_argument("-d", "--delay", type=int, default=1, help="Задержка опроса в секундах")

    # 4. Добавляем флаг-переключатель (true/false)
    parser.add_argument("--verbose", action="store_true", help="Включить детальный лог")

    # Парсим аргументы из sys.argv
    args = parser.parse_args()

    # Доступ к переменным идет через точку: args.имя_параметра
    print(f"Запуск опроса для: {args.sensor_id}")
    print(f"Настройки: задержка={args.delay}с, детальный лог={args.verbose}")

if __name__ == "__main__":
    main()