class Sensor:
    def __init__(self, sensor_id: str, sensor_type: str):
        self.sensor_id = sensor_id  # public-поле
        self._status = "active"  # protected-поле (одно подчеркивание _)
        self.__internal_key = "123x"  # private-поле (два подчеркивания __)
        self.__sensor_type = sensor_type  # public-поле

    # 2. Обычный метод класса
    def get_info(self) -> str:
        return f"Датчик {self.sensor_id} имеет статус: {self._status}, тип: {self.__sensor_type}, внутренний ключ: {self.__internal_key}"


newSensor = Sensor("S001", "temperature")
sensor_info = newSensor.get_info()
print(sensor_info)


class Simple:
    def __init__(self):
        self.a = 1  # Поле 'a' создалось тут


obj = Simple()

# А теперь внимание: поля 'b' вообще не существует в классе!
# Но мы пишем:
obj.b = 99  # Python молча создал поле 'b' прямо на лету для этого объекта!

print(obj.b)  # Выведет: 99
