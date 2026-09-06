import threading
import time

def read_sensor(sensor_name):
    print(f"Читаем {sensor_name}")
    time.sleep(2)
    print(f"Данные из {sensor_name} получены ")

t1 = threading.Thread(target=read_sensor, args=("Датчик 1",))
t2 = threading.Thread(target=read_sensor, args=("Датчик 2",))

t1.start()
t2.start()

t1.join()
t2.join()
print("Все датчики опрошены! Можно сохранить данные в базу.")