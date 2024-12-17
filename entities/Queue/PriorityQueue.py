from heapq import heappush, heappop
from typing import Optional, TypeVar
from .QueueItem import QueueItem
from .Queue import Queue

T = TypeVar("T")

class PriorityQueue(Queue[T]):
    def __init__(self, max_size: Optional[int] = None):
        super().__init__(max_size)
        self.queue = []
    def enqueue(self, item: QueueItem[T]) -> Optional[QueueItem[T]]:
        if self.is_full():
            self.rejected_count += 1
            return
        heappush(self.queue, item)
        return item

    def dequeue(self, wait_time: float) -> Optional[QueueItem[T]]:
        if self.is_empty():
            return
        item = heappop(self.queue)
        item.set_wait_time(wait_time)
        return item

    def peek(self) -> Optional[QueueItem[T]]:
        if self.is_empty():
            return None
        return self.queue[0]

    def __str__(self):
        return f"PriorityQueue: {[item for item in self.queue]}"
