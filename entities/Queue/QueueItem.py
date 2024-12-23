from typing import Generic, TypeVar, Optional, Literal
from time import time

T = TypeVar("T")
Priority = Literal[0, 1]

class QueueItem(Generic[T]):
    def __init__(self, entity: T, entry_time: int, priority: Optional[Priority] = None):
        self.entity = entity
        self.priority = priority
        self.entry_time = entry_time
        self.wait_time: Optional[float] = None

    def set_wait_time(self, wait_time: float) -> None:
        self.wait_time = wait_time

    def __lt__(self, other: "QueueItem[T]") -> bool:
        if self.priority is None and other.priority is None:
            return self.entry_time < other.entry_time
        if self.priority is None:
            return False
        if other.priority is None:
            return True
        return self.priority > other.priority

    def __repr__(self):
        priority_repr = (
            "No priority" if self.priority is None
            else "Child" if self.priority == 1
            else "Adult"
        )
        wait_time_repr = f"{self.wait_time:.2f}" if self.wait_time is not None else "Not set"
        entry_time_repr = self.entry_time
        return f"\n{self.entity} ({priority_repr}, wait time: {wait_time_repr}, entry time: {entry_time_repr})"

    @staticmethod
    def define_priority(age: float) -> Priority:
        return 1 if age < 18 else 0