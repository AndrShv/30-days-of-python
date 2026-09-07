from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict, BaseModel


class PDF_request(BaseModel):
    title: str
    file_path: str


class PDF_response(BaseModel):
    id: UUID
    title: str
    file_path: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
