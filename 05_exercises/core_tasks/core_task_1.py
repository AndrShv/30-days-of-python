# Задача 1. Слайсы (Срезы) строк и списков
log = "2026-07-17_ID-9941_TEMP-24.5"
print(log[0:10]) # date
print(log[14:18]) # id
print(log[::-1])

# Задача 2. Генераторы списков (List Comprehensions)

raw_data = [
    {"sensor": "T01", "temp": 21.5},
    {"sensor": "T02", "temp": -5.0},  # Датчик сбоит или на улице мороз
    {"sensor": "T03", "temp": 28.3},
    {"sensor": "T04", "temp": -1.2}
]

filtered_data = [item["temp"] for item in raw_data if item["temp"] > 0]
print(filtered_data)


# Задача 3. Безопасные словари и дефолты

settings = {
    "mode": "manual",
    "frequence_minutes": 30
}

auto_watering_param = settings.get("auto_watering", False)
print(auto_watering_param)
settings.setdefault("auto_watering", False)
print(settings)

