
def sensor_logs_generator(sensor_id: str, count: int):
    for i in range(1, count+1):
      yield f"Sensor ID: {sensor_id}, Log Entry: {i}"

sensor_logs = sensor_logs_generator("S001", 5)

for log in sensor_logs:
    print(log)

