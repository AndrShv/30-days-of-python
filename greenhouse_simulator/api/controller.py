from fastapi import FastAPI, Depends, HTTPException
from greenhouse_simulator.dto.data_transf_objcts import SensorRequest, SensorResponse
from sqlalchemy.orm import Session
from greenhouse_simulator.db.db_model import DBTargetSensor, get_db
from greenhouse_simulator.utils.processors import sensor_data_stream
from greenhouse_simulator.main import app



@app.post("/sensors/data", status_code=201, response_model=SensorResponse)
def create_sensor_data(sensor_in: SensorRequest, db: Session = Depends(get_db)):
    db_sensor = db.query(DBTargetSensor).filter(DBTargetSensor.name == sensor_in.name).first()
    if db_sensor:
        raise HTTPException(status_code=400, detail="Датчик с таким именем уже существует")
    new_sensor = DBTargetSensor(**sensor_in.model_dump())
    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)
    return new_sensor


@app.get("/sensors/data", response_model=list[SensorResponse])
def get_all_sensors(db: Session = Depends(get_db)):
    return db.query(DBTargetSensor).all()


@app.get("/sensors/data/{sensor_id}", response_model=SensorResponse)
def get_sensor_by_id(sensor_id: int, db: Session = Depends(get_db)):
    return db.query(DBTargetSensor).filter(DBTargetSensor.id == sensor_id).first()

@app.get("/sensors/analytics", response_model=list[SensorResponse])
def get_analytics(db: Session = Depends(get_db)):
    all_sensors = db.query(DBTargetSensor).all()
    filtered_data = sensor_data_stream(all_sensors)
    return filtered_data


