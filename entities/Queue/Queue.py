from collections import deque
from typing import Optional, Generic, TypeVar
from .QueueItem import QueueItem

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self, max_size: Optional[int] = None):
        self.queue = deque[QueueItem[T]]()
        self.max_size = max_size
        self.rejected_count = 0

    def is_full(self) -> bool:
        return self.max_size is not None and len(self.queue) >= self.max_size

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def enqueue(self, item: QueueItem[T]) -> Optional[QueueItem[T]]:
        if self.is_full():
            self.rejected_count += 1
            return
        self.queue.append(item)
        return item

    def dequeue(self, wait_time: float) -> Optional[QueueItem[T]]:
        if self.is_empty():
            return None
        item = self.queue.popleft()
        item.set_wait_time(wait_time)
        return item

    def peek(self) -> Optional[QueueItem[T]]:
        if self.is_empty():
            return None
        return self.queue[0]

    def size(self) -> int:
        return len(self.queue)

    def get_rejected_count(self) -> int:
        return self.rejected_count

    def __str__(self):
        return f"Queue: {[item for item in self.queue]}"
