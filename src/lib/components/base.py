from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, actor, update_order=1):
        self.actor = actor
        self.update_order = update_order

    def process_input(self, input_state) -> None:
        pass

    def update(self, delta_time):
        pass

    def destroy(self):
        pass
