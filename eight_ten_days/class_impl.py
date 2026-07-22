# Родительский (базовый) класс
class Sensor:
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self.status = "active"

    def get_info(self):
        return f"Датчик {self.sensor_id} работает."


# Дочерний класс (наследует всё от Sensor)
class TemperatureSensor(Sensor):
    def __init__(self, sensor_id: str, temperature: float):
        # Вызов конструктора родителя (аналог super() в Java)
        super().__init__(sensor_id)
        # Добавляем собственное уникальное свойство
        self.temperature = temperature

    # Переопределение метода (Method Overriding)
    def get_info(self):
        return f"Датчик {self.sensor_id} показывает температуру: {self.temperature}°C"


print("Пример использования классов:")
sensor1 = Sensor("S001")
temp_sensor1 = TemperatureSensor("T001", 25.0)

print(sensor1.get_info())  # Выводит: Датчик S001 работает.
print(temp_sensor1.get_info())  # Выводит: Датчик T001 показывает температуру: 25.0°C


class Editable:
    def edit(self):
        print("Редактируем данные")


class Loggable:
    def log(self):
        print("Записываем лог в файл")


# Класс наследует свойства и методы ОБОИХ родителей!
class DBRecord(Editable, Loggable):
    pass


record = DBRecord()
record.edit()  # Работает!
record.log()  # Работает!
