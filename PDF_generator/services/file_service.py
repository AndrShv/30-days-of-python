import logging
from PDF_generator.repo.file_repo import FileRepo
from PDF_generator.services.celery_worker import create_pdf_from_word_file

logger = logging.getLogger(__name__)

class FileService:
    def __init__(self, file_repo: FileRepo):
        self.file_repo = file_repo

    async def start_pdf_conversion(self, celery_path: str) -> str:
        logger.info(f"Submitting PDF conversion task for: {celery_path}")
        task = create_pdf_from_word_file.delay(celery_path)
        return task.id