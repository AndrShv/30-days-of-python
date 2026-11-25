from typing import Dict, Any
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class RawLog:
    event_id: int
    payload: str
    metadata: Dict[str, Any]



@dataclass(frozen=True)
class User:
    id: int
    username: str
