from entities.Queue.PriorityQueue import PriorityQueue
from entities.Customer.CustomerGenerator import CustomerGenerator
from entities.Connector.EntityGeneratorPriorityQueueConnector import EntityGeneratorPriorityQueueConnector
from entities.State.SystemState import state

simulation_time = 10

if __name__ == "__main__":
    # Використовуємо єдиний стан системи
    entity_state = state.entity_generators_state

    # Ініціалізація генераторів
    priority_customer_generator = CustomerGenerator(simulation_time, 1, (1, 17), entity_state)
    regular_customer_generator = CustomerGenerator(simulation_time, 1, (18, 100), entity_state)

    # Генеруємо клієнтів
    priority_customers = priority_customer_generator.run()
    regular_customers = regular_customer_generator.generate_customers()

    print("Priority Customers:", priority_customers)
    print("Regular Customers:", regular_customers)
    print("Priority Customers number:", len(priority_customers))
    print("Regular Customers number:", len(regular_customers))

    # Конектор для передачі клієнтів у чергу
    connector = EntityGeneratorPriorityQueueConnector(priority_customers, regular_customers)
    connector.process()

    # Виведення стану пріоритетної черги
    print("\nFinal Priority Queue State:")
    print(connector.destination)
