class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"🔌 [__enter__] Подключаемся к базе данных '{self.db_name}'...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("🔒 [__exit__] Сессия завершена. Безопасно закрываем коннект к БД.")
        return True


with DatabaseConnection("greenhouse_db") as db:
    print("      🚀 Выполняем SQL-запрос: SELECT * FROM sensors;")
