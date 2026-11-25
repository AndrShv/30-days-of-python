from __future__ import annotations

import logging

from fastapi import APIRouter

from rabbitmq_example.dto import Video
from rabbitmq_example.producer import produce_video_to_text_task

api_router = APIRouter()
logger = logging.getLogger(__name__)



@api_router.post("/video-to-text")
async def video_to_text(video_data: Video):
    logger.info(f"[REST] 📥 Получена заявка на конвертацию видео в текст: {video_data.url}")
    await produce_video_to_text_task(video_data)
    return {"message": "Video processing task sent to the queue"}



async def convert_video_to_text(video_data: Video) -> str | dict:
    logger.info(f"[REST] ⚙️  Начата обработка видео в текст: {video_data.url}")
    url = video_data.url
    title = video_data.title

    if url == "":
        logger.error("Video URL is required")
        return {"error": "Video URL is required"}

    text_from_video = title + " " + url
    logger.info(f"[REST] 📝 Результат обработки: {text_from_video}")
    return text_from_video



