from abc import ABC, abstractmethod
from typing import Any

class BaseConnector(ABC):
    def __init__(self, source: Any, destination: Any):
        self.source = source
        self.destination = destination

    @abstractmethod
    def process(self):
        pass
