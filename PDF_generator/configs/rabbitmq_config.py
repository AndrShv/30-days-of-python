from __future__ import annotations

import logging
import os

from aio_pika import RobustConnection, RobustChannel

from PDF_generator.dto import ProductDTO

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
QUEUE_NAME = os.getenv("QUEUE_NAME", "video_to_text")
logger = logging.getLogger(__name__)

rabbitmq_connection: RobustConnection | None = None
rabbitmq_channel: RobustChannel | None = None


async def create_check_price_event(product_data: ProductDTO):
    pass


