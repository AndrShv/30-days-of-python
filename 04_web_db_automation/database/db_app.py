from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel, Field
from typing import List

DATABASE_URL = "postgresql://greenhouse_user:greenhouse_secure_pass@localhost:5432/greenhouse_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class DBTargetSensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    zone = Column(String, nullable=False)
    current_value = Column(Float, default=0.0)
    is_online = Column(Boolean, default=True)


Base.metadata.create_all(bind=engine)


class SensorCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=20)
    zone: str = Field(..., min_length=2)
    current_value: float = Field(default=0.0)


class SensorResponse(SensorCreate):
    id: int
    is_online: bool

    class Config:
        from_attributes = True

app = FastAPI(title="Greenhouse DB API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# POST: Создание датчика
@app.post("/api/v1/sensors", response_model=SensorResponse, status_code=status.HTTP_201_CREATED)
def create_sensor(sensor_in: SensorCreate, db: Session = Depends(get_db)):
    db_sensor = db.query(DBTargetSensor).filter(DBTargetSensor.name == sensor_in.name).first()
    if db_sensor:
        raise HTTPException(status_code=400, detail="Датчик с таким именем уже существует")
    new_sensor = DBTargetSensor(**sensor_in.model_dump())

    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)
    return new_sensor


# GET: Получить все датчики из базы
@app.get("/api/v1/sensors", response_model=List[SensorResponse])
def get_all_sensors(db: Session = Depends(get_db)):
    # Аналог findAll()
    return db.query(DBTargetSensor).all()