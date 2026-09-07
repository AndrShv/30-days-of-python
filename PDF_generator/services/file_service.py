import logging

from PDF_generator.repo.file_repo import FileRepo
from PDF_generator.services.celery_worker import create_pdf_from_word_file

logger = logging.getLogger(__name__)

class FileService:
    def __init__(self, file_repo: FileRepo):
        self.file_repo = file_repo

    async def create_pdf_from_word(self, file_path: str):
        logger.info(f"Creating PDF from Word file: {file_path}")
        result = create_pdf_from_word_file.delay(file_path)
        return {"task_id": result.id, "status": "Task submitted for PDF generation"}
