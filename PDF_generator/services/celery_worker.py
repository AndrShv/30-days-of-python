import asyncio
import logging
import os
import subprocess

from PDF_generator.configs import celery_config
from PDF_generator.configs.db_config import AsyncSessionLocal
from PDF_generator.models.db_models import DBPdfFile
from PDF_generator.repo.file_repo import FileRepo

logger = logging.getLogger(__name__)




def convert_docx_to_pdf(file_path: str) -> str:
    logger.info(f"Начало конвертации файла: {file_path}")

    if not os.path.exists(file_path):
        error_msg = f"Файл не найден: {file_path}"
        logger.error(error_msg)
        raise FileNotFoundError(error_msg)

    output_dir = os.path.dirname(file_path) or "."

    command = [
        "libreoffice",
        "--headless",
        "--convert-to", "pdf",
        "--outdir", output_dir,
        file_path
    ]

    try:
        subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        base_name = os.path.splitext(os.path.basename(file_path))[0]
        pdf_path = os.path.join(output_dir, f"{base_name}.pdf")

        logger.info(f"Успешно сгенерирован PDF: {pdf_path}")
        return pdf_path

    except subprocess.CalledProcessError as exc:
        logger.error(f"Ошибка при вызове LibreOffice: {exc.stderr}")
        raise exc


async def _save_pdf_to_db(file_path: str, pdf_path: str) -> DBPdfFile:
    async with AsyncSessionLocal() as session:
        file_repo = FileRepo(session)

        db_file_to_save = DBPdfFile(
            title=os.path.basename(file_path),
            file_path=pdf_path
        )
        saved_file = await file_repo.create_file(db_file_to_save)
        return saved_file

@celery_config.celery_app.task(bind=True, max_retries=3, default_retry_delay=5, name='convert_word_to_pdf_task')
def create_pdf_from_word_file(self, file_path: str):
    logger.info(f"Starting PDF generation for file: {file_path}")
    try:
        pdf_path = convert_docx_to_pdf(file_path)
        logger.info(f"PDF generation completed for file: {file_path}")

        saved_file = asyncio.run(_save_pdf_to_db(file_path, pdf_path))
        return str(saved_file.file_path)

    except Exception as exc:
        logger.error(f"Error occurred while generating PDF for file: {file_path}: {exc}")
        raise self.retry(exc=exc)
