from decorator.Decorator import Decorator
from const import CONSUMPTION_COEFFICIENT, SUPPLY_COEFFICIENT, EXTRA_SUPPLY_COST
import copy


class SupplyDecorator(Decorator):
    def __init__(self, unit: Decorator):
        contents = copy.copy(unit.components)
        contents[6] *= CONSUMPTION_COEFFICIENT
        contents[3] *= SUPPLY_COEFFICIENT
        contents[2] += EXTRA_SUPPLY_COST
        super().__init__(contents)
