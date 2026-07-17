from fastapi import FastAPI
from pydantic import BaseModel

# 1. Создаем экземпляр приложения (аналог SpringApplication)
app_example = FastAPI(title="Smart Home API")


# 2. Описываем класс входных данных (как DTO в Java)
# Наследуемся от BaseModel из Pydantic — теперь это умная модель-валидатор!
class SensorReading(BaseModel):
    sensor_id: str
    temperature: float


# Временная "база данных" прямо в оперативной памяти
db_readings = []


# 3. GET-эндпоинт для получения всех записей
@app_example.get("/readings")
def get_all_readings():
    return {"status": "success", "data": db_readings}


# 4. POST-эндпоинт для отправки новых показаний датчика
@app_example.post("/readings")
def create_reading(reading: SensorReading):
    # Метод .dict() (или .model_dump() в новых версиях) превращает объект класса в обычный словарь Python dict
    db_readings.append(reading.model_dump())
    return {"status": "created", "added_reading": reading}
