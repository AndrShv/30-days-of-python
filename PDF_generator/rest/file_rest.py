import logging

from fastapi_utils.cbv import cbv
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from PDF_generator.configs.db_config import get_db_session
from PDF_generator.repo.file_repo import FileRepo
from PDF_generator.services.file_service import FileService
from PDF_generator.services.path_service import resolve_file_path_for_celery
from PDF_generator.services.celery_worker import create_pdf_from_word_file
file_router = APIRouter(prefix="/api/v1/file", tags=["File"])
logger = logging.getLogger(__name__)


def get_file_service(session: AsyncSession = Depends(get_db_session)) -> FileService:
    return FileService(FileRepo(session))


@cbv(file_router)
class FileRestController:
    file_service: FileService = Depends(get_file_service)

    @file_router.post("/convert/{file_path:path}")
    async def create_file(self, file_path: str):
        if not file_path.startswith("/"):
            file_path = "/" + file_path

        celery_path = resolve_file_path_for_celery(file_path)
        task = create_pdf_from_word_file.delay(celery_path)

        return {
            "status": "processing",
            "task_id": task.id,
            "original_path": file_path,
            "container_path": celery_path
        }