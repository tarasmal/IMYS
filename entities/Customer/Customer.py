class Customer:
    def __init__(self, number: int, age: int):
        self.name = f"CU_{number}"
        self.age = age

    def __repr__(self):
        return f"{self.name} (Age: {self.age})"
