from abc import ABC, abstractmethod
from base.Unit import Unit


class UnitBuilder(ABC):

    @abstractmethod
    def add_sprite(self):
        pass

    @abstractmethod
    def add_dying_sprite(self):
        pass

    @abstractmethod
    def add_cost(self):
        pass

    @abstractmethod
    def add_hp(self):
        pass

    @abstractmethod
    def add_damage(self):
        pass

    @abstractmethod
    def add_blow_damage(self):
        pass

    @abstractmethod
    def add_consumption(self):
        pass

    @abstractmethod
    def get_unit(self) -> Unit:
        pass
