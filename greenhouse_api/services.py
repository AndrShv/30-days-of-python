from fastapi import FastAPI
from models import GreenHouse, FixRequest
import database


app = FastAPI(title="GreenHouse API")


@app.get("/all")
def get_all_green_houses():
    print("Getting all GreenHouses")
    return database.get_all_green_houses()

@app.post("/greenHouse")
def create_green_house(greenHouse: GreenHouse):
    database.add_green_house(greenHouse)
    return {"status": "created",
            "sensor_id": greenHouse.sensor_id,
            "temperature": greenHouse.temperature,
            "humidity": greenHouse.humidity
            }

@app.get("/dry-zones")
def get_dry_zones():
    print("Getting all dry zones")
    return database.get_dry_zones()

@app.get("/fix-zones")
def get_fix_zones():
    print("Getting all fix zones")
    return database.get_fix_zones()

@app.put("/fix")
def fix_green_house(request_data: FixRequest):
    print("Fixing green house")
    database.fix_green_house(request_data.sensor_id)
    return {
        "status": "fixed",
        "sensor_id": request_data.sensor_id,
    }

