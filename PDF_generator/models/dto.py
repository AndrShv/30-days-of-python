from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict


class PDF_request:
    title: str
    file_path: str


class PDF_response:
    id: UUID
    title: str
    file_path: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
