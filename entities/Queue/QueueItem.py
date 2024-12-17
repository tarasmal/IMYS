from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class QueueItem(Generic[T]):
    def __init__(self, entity: T, priority: Optional[int] = None):
        self.entity = entity
        self.priority = priority
        self.wait_time: Optional[float] = None

    def set_wait_time(self, wait_time: float) -> None:
        self.wait_time = wait_time

    def __lt__(self, other: "QueueItem[T]") -> bool:
        if self.priority is None or other.priority is None:
            raise ValueError("Priority is not set. To compare, both items must have a priority.")
        return self.priority < other.priority

    def __repr__(self):
        priority_repr = f"Priority: {self.priority}" if self.priority is not None else "No priority"
        wait_time_repr = f"{self.wait_time:.2f}" if self.wait_time is not None else 0
        return f"{self.entity} ({priority_repr}, wait time: {wait_time_repr})"
