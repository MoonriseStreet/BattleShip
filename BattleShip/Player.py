import arcade
import const
from base.Unit import Unit
from builder.BoatUnitBuilder import BoatUnitBuilder
from builder.CruiserUnitBuilder import CruiserUnitBuilder
from builder.FrigateUnitBuilder import FrigateUnitBuilder


class Player(object):
    def __init__(self):
        self.money = const.INIT_MONEY
        self.builders = [BoatUnitBuilder(), FrigateUnitBuilder(),
                         CruiserUnitBuilder()]
        for i in range(3):
            self.builders[i].add_sprite()
            self.builders[i].add_dying_sprite()
            self.builders[i].add_cost()
            self.builders[i].add_hp()
            self.builders[i].add_damage()
            self.builders[i].add_blow_damage()
            self.builders[i].add_consumption()
        self.curr = None

    def set_builder(self, number: int):
        self.curr = number

    def clone(self) -> Unit:
        return self.builders[self.curr].get_unit()

    def draw(self):
        if self.money <= 200:
            color = arcade.color.AUBURN
        else:
            color = arcade.color.COOL_BLACK

        if self.money < 100:
            length = 80
        elif self.money < 1000:
            length = 120
        else:
            length = 160

        arcade.draw_text(str(self.money) + ' $', const.MONEY_BAR_X, const.MONEY_BAR_Y,
                         color, 22, length, anchor_x="center",
                         font_name=const.FONT_NAME)

    def money_decrease(self, cost):
        self.money = max(0, self.money - cost)