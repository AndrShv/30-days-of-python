class GreenhouseSession:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"--- Открываем сессию мониторинга теплицы {self.name} ---")
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"--- Сессия для {self.name} успешно закрыта ---")

with GreenhouseSession("Greenhouse1") as session:
    print(f"Система считывает показатели влажности и температуры...")

