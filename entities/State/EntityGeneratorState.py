import threading

from entities.decorators.singleton import singleton


@singleton
class EntityGeneratorsState:
    def __init__(self):
        self.current_entry_time: int = 1
        self.lock = threading.Lock()

    def get_and_increment_entry_time(self) -> int:
        with self.lock:
            entry_time = self.current_entry_time
            self.current_entry_time += 1
            return entry_time
