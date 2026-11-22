from __future__ import annotations

import logging
import os

from aio_pika import RobustConnection, RobustChannel


RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
QUEUE_NAME = os.getenv("QUEUE_NAME", "video_to_text")
logger = logging.getLogger(__name__)

rabbitmq_connection: RobustConnection | None = None
rabbitmq_channel: RobustChannel | None = None




