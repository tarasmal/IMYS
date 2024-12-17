from entities.Queue.Queue import Queue
from entities.Queue.QueueItem import QueueItem

if __name__ == "__main__":
    print("=== Testing Queue with Wait Time ===\n")

    queue = Queue[str](max_size=3)

    print("Enqueuing QueueItems:")
    queue.enqueue(QueueItem("Client 1"))
    queue.enqueue(QueueItem("Client 2"))
    queue.enqueue(QueueItem("Client 3"))

    print("\nCurrent queue state:")
    print(queue)

    print("\nDequeuing with wait times:")
    print("Dequeued:", queue.dequeue(wait_time=5))
    print("Dequeued:", queue.dequeue(wait_time=3))
    print("Dequeued:", queue.dequeue(wait_time=0))

    print("\nFinal queue state:")
    print(queue)
