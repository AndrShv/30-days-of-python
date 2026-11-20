from __future__ import annotations

from typing import Callable, TypeVar, Generic

# Java: List<String> names = new ArrayList<>();
# Python 3.10+:
names: list[str] = ["Andrey", "Alexander"]

# Java: Optional<User> user = ... / User | null
# Python 3.10+:
user: User | None = find_user(user_id=10)

# Generic тип (Аналог T в Java: class Repository<T>)
T = TypeVar("T")

class BaseRepository(Generic[T]):
    def get_by_id(self, entity_id: str) -> T | None:
        ...