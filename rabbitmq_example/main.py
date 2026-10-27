import os
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from aio_pika import connect_robust

from rabbitmq_example.rest_controller import api_router
from rabbitmq_example import producer

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")


@asynccontextmanager
async def lifespan(app: FastAPI):
    producer.rabbitmq_connection = await connect_robust(RABBITMQ_URL)
    producer.rabbitmq_channel = await producer.rabbitmq_connection.channel()
    await producer.rabbitmq_channel.declare_queue(producer.QUEUE_NAME, durable=True)
    print("✅ Успешное подключение к RabbitMQ при старте FastAPI")
    yield
    await producer.rabbitmq_connection.close()
    print("🛑 Соединение с RabbitMQ закрыто")


app = FastAPI(title="RabbitMQ + FastAPI Demo", lifespan=lifespan)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("rabbitmq_example.main:app", host="127.0.0.1", port=8001, reload=True)