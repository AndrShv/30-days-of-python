import uvicorn
from fastapi import FastAPI
from greenhouse_simulator.api.controller import router as sensors_router

app = FastAPI(title="Greenhouse Service API")
app.include_router(sensors_router, prefix="/api")
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)