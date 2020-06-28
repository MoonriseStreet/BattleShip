from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def on_update(self, delta_time, info: list):
        pass

    @abstractmethod
    def new_unit(self) -> int:
        pass
