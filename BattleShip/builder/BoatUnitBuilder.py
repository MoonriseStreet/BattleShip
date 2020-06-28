import const
from base.Unit import Unit
from builder.UnitBuilder import UnitBuilder


class BoatUnitBuilder(UnitBuilder):
    def __init__(self):
        super().__init__()
        self._contents = []

    def add_sprite(self):
        self._contents.append(const.SHIPS_IMAGE[0][0])

    def add_dying_sprite(self):
        self._contents.append(const.SHIPS_IMAGE[0][1])

    def add_cost(self):
        self._contents.append(const.SHIPS_COST[0])

    def add_hp(self):
        self._contents.append(const.SHIPS_HP[0])

    def add_damage(self):
        self._contents.append(const.SHIPS_DAMAGE[0])

    def add_blow_damage(self):
        self._contents.append(const.SHIPS_BLOW_DAMAGE[0])

    def add_consumption(self):
        self._contents.append(const.SHIPS_CONSUMPTION[0])

    def get_unit(self) -> Unit:
        return Unit(self._contents)
