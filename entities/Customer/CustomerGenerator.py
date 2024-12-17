import random
from typing import List, Tuple
from .Customer import Customer

class CustomerGenerator:
    def __init__(self, simulation_time: int, lambda_rate: float, age_range: Tuple[int, int]):
        self.simulation_time = simulation_time
        self.lambda_rate = lambda_rate
        self.age_range = age_range
        self.counter = 1

    def poisson_arrivals(self) -> List[int]:
        current_time = 0
        arrival_times = []
        while current_time < self.simulation_time:
            interval = random.expovariate(self.lambda_rate)
            current_time += interval
            if current_time <= self.simulation_time:
                arrival_times.append(current_time)
        return arrival_times

    def generate_customers(self) -> List[Customer]:
        arrival_times = self.poisson_arrivals()
        customers = []
        for _ in arrival_times:
            age = random.randint(*self.age_range)
            customers.append(Customer(number=self.counter, age=age))
            self.counter += 1
        return customers
