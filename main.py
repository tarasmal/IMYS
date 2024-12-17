from entities.Queue.Queue import Queue
from entities.Queue.QueueItem import QueueItem
from entities.Queue.PriorityQueue import  PriorityQueue
from entities.Customer.CustomerGenerator import CustomerGenerator
simulation_time = 50
if __name__ == "__main__":
    priority_customer_generator = CustomerGenerator(simulation_time, 1.5, (1, 17))
    regular_customer_generator = CustomerGenerator(simulation_time, 1.5, (18, 100))
    priority_customers = priority_customer_generator.generate_customers()
    regular_customers = regular_customer_generator.generate_customers()
    print(priority_customers)
    print(regular_customers)
    print("Priority Customers number: ", len(priority_customers))
    print("Regular Customers number: ", len(regular_customers))
    # print("=== Testing Queue witout priority ===\n")
    #
    # queue = Queue[str](max_size=3)
    #
    # print("Enqueuing QueueItems:")
    # print("Queued:", queue.enqueue(QueueItem("Client 1", 1, priority=0)))
    # print("Queued:", queue.enqueue(QueueItem("Client 2", 2, priority=1)))
    # print("Queued:", queue.enqueue(QueueItem("Client 3", 3, priority=0)))
    #
    # print("\nCurrent queue state:")
    # print(queue)
    #
    # print("\nDequeuing with wait times:")
    # print("Dequeued:", queue.dequeue(wait_time=5))
    # print("Dequeued:", queue.dequeue(wait_time=3))
    # print("Dequeued:", queue.dequeue(wait_time=0))
    #
    # print("\nFinal queue state:")
    # print(queue)
    #
    # print("=== Testing PriorityQueue with Different Priorities ===\n")
    #
    # priority_queue = PriorityQueue[str](max_size=6)
    #
    # print("Queued:", priority_queue.enqueue(QueueItem("Client 1", 1, priority=0)))
    # print("Queued:", priority_queue.enqueue(QueueItem("Client 2", 2, priority=1)))
    # print("Queued:", priority_queue.enqueue(QueueItem("Client 3", 3, priority=0)))
    #
    # print("Current Priority Queue State:")
    # print(priority_queue)
    #
    # print("\nDequeuing elements:")
    # wait_time = 0
    # while not priority_queue.is_empty():
    #     item = priority_queue.dequeue(wait_time=wait_time)
    #     print("Dequeued:", item)
    #     wait_time += 5
    #
    # print("\nFinal Priority Queue State:")
    # print(priority_queue)