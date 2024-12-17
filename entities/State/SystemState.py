from entities.State.EntityGeneratorState import EntityGeneratorsState
from entities.decorators.singleton import singleton


@singleton
class SystemState:
    def __init__(self):
        self.entity_generators_state = EntityGeneratorsState()

state = SystemState()