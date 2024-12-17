from .BaseConnector import BaseConnector
from typing import List

from ..Customer.Customer import Customer
from ..Queue.QueueItem import QueueItem
from ..Queue.PriorityQueue import PriorityQueue


class EntityGeneratorPriorityQueueConnector(BaseConnector):
    def __init__(self, priority_customers: List[Customer], regular_customers: List[Customer]):
        source = priority_customers + regular_customers
        destination = PriorityQueue()
        super().__init__(source, destination)

    def process(self):
        for index, customer in enumerate(self.source):
            priority = QueueItem.define_priority(age=customer.age)
            queue_item = QueueItem(entity=customer, entry_time=customer.entry_time, priority=priority)
            self.destination.enqueue(queue_item)