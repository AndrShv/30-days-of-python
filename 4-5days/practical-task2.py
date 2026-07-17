import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared import average, parse_kv_record  # noqa: E402

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
        record = parse_kv_record(sensor, ";")
        name = record["id"]
        temp = float(record["val"])
        condition = record["status"]
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
        temp_value = float(parse_kv_record(sensors, ";")["val"])
        temperatures.append(temp_value)

    if temperatures:
        avg_temp = average(temperatures)
        print(f"Average temperature of active sensors: {avg_temp:.2f}°C")
    else:
        print("No active sensors found.")


filter_active_sensors(raw_sensors_data)

count_avg_temp(active_sensors)


print("Active sensors", active_sensors)
