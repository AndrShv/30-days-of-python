import asyncio
import logging
from fastapi import APIRouter

from config import celery_app

fast_api_app = APIRouter()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def async_send_email_logic(user_email: str):
    logger.info(f"[Async Core] Начинаем асинхронную отправку для {user_email}...")
    await asyncio.sleep(3)
    logger.info(f"[Async Core] Письмо успешно ушло на {user_email}!")
    return f"Email sent to {user_email}"


@celery_app.task(bind=True, max_retries=3, default_retry_delay=5, name="send_welcome_email")
def send_welcome_email(self, user_email: str):
    logger.info(f"[Worker] Получена задача Celery для {user_email}")

    try:
        result = asyncio.run(async_send_email_logic(user_email))
        logger.info("Result was successfully returned")
        return result

    except Exception as exc:
        logger.warning(f"[Worker] Ошибка: {exc}. Повтор задачи...")
        raise self.retry(exc=exc)


@fast_api_app.post("/send_welcome_email/{email}")
async def send_welcome_email_task(email: str):
    logger.info(f"Attempt to send welcome email by user email: {email}")
    task = send_welcome_email.delay(email)
    return {
        "status": "Task dispatched to queue",
        "task_id": task.id,
        "email": email
    }