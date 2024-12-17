class Customer:
    def __init__(self, number: int, age: float, entry_time: int):
        self.name = f"CU_{number}"
        self.age = age
        self.entry_time = entry_time

    def __repr__(self):
        return f"{self.name} (Age: {self.age})"
