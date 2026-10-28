from __future__ import annotations

import json
import logging
import os
from aio_pika import Message, DeliveryMode, RobustConnection, RobustChannel

from rabbitmq_example.dto import Video

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
QUEUE_NAME = os.getenv("QUEUE_NAME", "video_to_text")
logger  = logging.getLogger(__name__)

rabbitmq_connection: RobustConnection | None = None
rabbitmq_channel: RobustChannel | None = None



async def produce_video_to_text_task(video_data: Video):
    global rabbitmq_channel
    if not rabbitmq_channel:
        raise RuntimeError("RabbitMQ channel is not initialized!")

    video_title, video_url = video_data.title, video_data.url
    logger.info(f"[Producer] 📤 Отправка задачи на конвертацию аудио в текст: {video_url}")
    message_body= {
        "video_url": video_url,
        "video_title": video_title,
        "action": "convert_to_text"
    }
    message = Message(
        body=json.dumps(message_body).encode("utf-8"),
        delivery_mode=DeliveryMode.PERSISTENT
    )
    logger.info(f"[Producer] 📤 Отправка задачи: {video_url}")
    await rabbitmq_channel.default_exchange.publish(message, routing_key=QUEUE_NAME)
    logger.info(f"[Producer] 📤 Отправлена задача: {video_url}")


