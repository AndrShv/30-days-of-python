from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List
from datetime import datetime

app = FastAPI(title="Greenhouse Automation", version="2.0.0")


class ValveCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Название клапана полива")
    zone: str = Field(..., description="Сектор теплицы")
    max_flow_rate: float = Field(..., gt=0, description="Максимальный расход воды (л/мин)")
    is_active: bool = Field(default=True)


class ValveResponse(ValveCreate):
    id: int
    last_opened: Optional[datetime] = None


# Временная база данных в памяти (In-Memory Simulation)
valves_db = []
id_counter = 1


# --- Эндпоинты ---

@app.post("/api/v1/valves", response_model=ValveResponse, status_code=status.HTTP_201_CREATED)
async def create_valve(valve: ValveCreate):
    global id_counter
    # Превращаем Pydantic-модель в обычный dict и добавляем системные поля
    new_valve_data = valve.model_dump()
    new_valve = ValveResponse(id=id_counter, **new_valve_data)

    valves_db.append(new_valve)
    id_counter += 1
    return new_valve


# GET: Получить все клапаны
@app.get("/api/v1/valves", response_model=List[ValveResponse])
async def get_all_valves():
    return valves_db


# GET: Получить один по ID (В путевом параметре автоматически проверяется тип int)
@app.get("/api/v1/valves/{valve_id}", response_model=ValveResponse)
async def get_valve(valve_id: int):
    for v in valves_db:
        if v.id == valve_id:
            return v
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Клапан с ID {valve_id} не найден"
    )