class IncidentRepository:
    def __init__(self, items: list[str]):
        self._items = items

    # Analog of len(repo)
    def __len__(self) -> int:
        return len(self._items)

    # Allows indexing: repo[0]
    def __getitem__(self, index: int) -> str:
        return self._items[index]

    # Context Manager (Java: try-with-resources / AutoCloseable)
    def __enter__(self):
        print("Opening DB connection...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing DB connection...")


# Использование Context Manager:
with IncidentRepository(["fire", "accident"]) as repo:
    print(len(repo))  # Вызовет __len__
    print(repo[0])    # Вызовет __getitem__