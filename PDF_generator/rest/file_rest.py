import logging
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from PDF_generator.configs.db_config import get_db_session
from PDF_generator.models.dto import TaskResponse
from PDF_generator.repo.file_repo import FileRepo
from PDF_generator.services.file_service import FileService
from PDF_generator.services.path_service import resolve_file_path_for_celery

file_router = APIRouter(prefix="/api/v1/file", tags=["File"])
logger = logging.getLogger(__name__)


def get_file_service(session: AsyncSession = Depends(get_db_session)) -> FileService:
    return FileService(FileRepo(session))


@file_router.post("/convert/{file_path:path}", response_model=TaskResponse, status_code=status.HTTP_202_ACCEPTED)
async def convert_file_to_pdf(file_path: str, file_service: FileService = Depends(get_file_service)):
    logger.info(f"Starting conversion for file: {file_path}")

    if not file_path.startswith("/"):
        file_path = "/" + file_path

    celery_path = resolve_file_path_for_celery(file_path)
    task_id = await file_service.start_pdf_conversion(celery_path)
    logger.info(f"Conversion task submitted for file: {file_path}, task_id: {task_id}")
    return TaskResponse(
        task_id=task_id,
        status="processing",
        original_path=file_path,
        container_path=celery_path
    )