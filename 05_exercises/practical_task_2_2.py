raw_sensors_data = [
    "  id:temp_01;val:23.5;status:active  ",
    "  id:hum_02;val:45.2;status:active  ",
    "  id:temp_03;val:19.8;status:inactive  ",
    "  id:temp_04;val:28.1;status:active  ",
    "  id:press_05;val:101.3;status:active  ",
    "  id:temp_06;val:0.0;status:error  ",
]
active_sensors = []


def filter_active_sensors(sensor_data):
    for sensor in sensor_data:
        striped_senor = sensor.strip()
        sensor_parts = striped_senor.split(";")
        id, val, status = sensor_parts
        name = id.split(":")[1]
        temp = float(val.split(":")[1])
        condition = status.split(":")[1]
        if condition == "active" and "temp" in name:
            active_sensors.append(sensor)
            sensor_data = [{"ID": name, "temp": temp, "condition": condition}]
    if sensor_data:
        print(
            f"ID: {sensor_data[0]['ID']}, Temp: {sensor_data[0]['temp']}, Condition: {sensor_data[0]['condition']}"
        )


def count_avg_temp(active_sensors):
    temperatures = []
    for sensors in active_sensors:
        striped_senor = sensors.strip()
        sensor_parts = striped_senor.split(";")
        temp_value = float(sensor_parts[1].split(":")[1])
        temperatures.append(temp_value)

    avg_temp = sum(temperatures) / len(temperatures)

    if len(temperatures) > 0:
        avg_temp = sum(temperatures) / len(temperatures)
        print(f"Average temperature of active sensors: {avg_temp:.2f}°C")
    else:
        print("No active sensors found.")


filter_active_sensors(raw_sensors_data)

count_avg_temp(active_sensors)


print("Active sensors", active_sensors)
