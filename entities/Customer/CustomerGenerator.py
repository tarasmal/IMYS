import random
import threading
from typing import Tuple, List
from .Customer import Customer
from ..State.EntityGeneratorState import EntityGeneratorsState


class CustomerGenerator(threading.Thread):
    def __init__(self, simulation_time: int, lambda_rate: float, age_range: Tuple[int, int],
                 state: EntityGeneratorsState, customer_list: List[Customer]):
        super().__init__()
        self.simulation_time = simulation_time
        self.lambda_rate = lambda_rate
        self.age_range = age_range
        self.state = state
        self.customer_list = customer_list

    def poisson_arrivals(self) -> List[float]:
        current_time = 0
        arrival_times = []
        while current_time < self.simulation_time:
            interval = random.expovariate(self.lambda_rate)
            current_time += interval
            if current_time <= self.simulation_time:
                arrival_times.append(current_time)
        return arrival_times

    def run(self):
        arrival_times = self.poisson_arrivals()
        for _ in arrival_times:
            age = random.randint(*self.age_range)
            entry_time = self.state.get_and_increment_entry_time()
            customer = Customer(number=entry_time, age=age, entry_time=entry_time)
            self.customer_list.append(customer)

