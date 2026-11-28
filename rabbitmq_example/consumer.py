import asyncio
import json
import logging
import os
from aio_pika import IncomingMessage, connect_robust
from rabbitmq_example.rest_controller import convert_video_to_text

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
QUEUE_NAME = os.getenv("QUEUE_NAME", "video_to_text")

logger  = logging.getLogger(__name__)

async def consume_video(message: IncomingMessage):
    async with message.process():
        data = json.loads(message.body.decode("utf-8"))
        video_url = data.get("video_url")
        print(f"[Consumer] ⚙️  Начата обработка аудио в текст: {video_url}")
        await convert_video_to_text(data)
        print(f"[Consumer] ✅ Аудио {video_url} успешно обработано!")





async def start_consumer():
    connection = await connect_robust(RABBITMQ_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue(QUEUE_NAME, durable=True)
    logger.info("[Consumer] 👂 Очередь прослушивается...")
    await queue.consume(consume_video)
    await asyncio.Future()
