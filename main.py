from entities.Queue.Queue import Queue
from entities.Queue.QueueItem import QueueItem
from entities.Queue.PriorityQueue import  PriorityQueue

if __name__ == "__main__":
    print("=== Testing Queue witout priority ===\n")

    queue = Queue[str](max_size=3)

    print("Enqueuing QueueItems:")
    print("Queued:", queue.enqueue(QueueItem("Client 1", 1, priority=0)))
    print("Queued:", queue.enqueue(QueueItem("Client 2", 2, priority=1)))
    print("Queued:", queue.enqueue(QueueItem("Client 3", 3, priority=0)))

    print("\nCurrent queue state:")
    print(queue)

    print("\nDequeuing with wait times:")
    print("Dequeued:", queue.dequeue(wait_time=5))
    print("Dequeued:", queue.dequeue(wait_time=3))
    print("Dequeued:", queue.dequeue(wait_time=0))

    print("\nFinal queue state:")
    print(queue)

    print("=== Testing PriorityQueue with Different Priorities ===\n")

    priority_queue = PriorityQueue[str](max_size=6)

    print("Queued:", priority_queue.enqueue(QueueItem("Client 1", 1, priority=0)))
    print("Queued:", priority_queue.enqueue(QueueItem("Client 2", 2, priority=1)))
    print("Queued:", priority_queue.enqueue(QueueItem("Client 3", 3, priority=0)))

    print("Current Priority Queue State:")
    print(priority_queue)

    print("\nDequeuing elements:")
    wait_time = 0
    while not priority_queue.is_empty():
        item = priority_queue.dequeue(wait_time=wait_time)
        print("Dequeued:", item)
        wait_time += 5

    print("\nFinal Priority Queue State:")
    print(priority_queue)