from decorators.Decorator import Decorator
from const import (CONSUMPTION_COEFFICIENT, WEAPON_COEFFICIENT, EXTRA_WEAPON_COST)
import copy


class WeaponDecorator(Decorator):
    def __init__(self, unit: Decorator):
        contents = copy.copy(unit.components)
        contents[6] *= CONSUMPTION_COEFFICIENT
        contents[4] *= WEAPON_COEFFICIENT
        contents[2] += EXTRA_WEAPON_COST
        super().__init__(contents)