from arcade import color, draw_text
from const import (INIT_MONEY, MONEY_BAR_X, MONEY_BAR_Y, FONT_NAME, MONEY_FONT_SIZE, ENOUGH_MONEY,
                   II_DIGIT_LENGTH, III_DIGIT_LENGTH, MORE_DIGIT_LENGTH, SHIPS_COUNT)
from base.Unit import Unit
from builder.BoatUnitBuilder import BoatUnitBuilder
from builder.CruiserUnitBuilder import CruiserUnitBuilder
from builder.FrigateUnitBuilder import FrigateUnitBuilder


class Player(object):
    def __init__(self):
        self.money = INIT_MONEY
        self.builders = [BoatUnitBuilder(), FrigateUnitBuilder(),
                         CruiserUnitBuilder()]
        for i in range(SHIPS_COUNT):
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
        if self.money <= ENOUGH_MONEY:
            curr_color = color.AUBURN
        else:
            curr_color = color.COOL_BLACK

        if self.money < 100:
            length = II_DIGIT_LENGTH
        elif self.money < 1000:
            length = III_DIGIT_LENGTH
        else:
            length = MORE_DIGIT_LENGTH

        draw_text(str(self.money) + ' $', MONEY_BAR_X, MONEY_BAR_Y, curr_color, MONEY_FONT_SIZE, length,
                  anchor_x="center", font_name=FONT_NAME)

    def money_decrease(self, cost):
        self.money = max(0, self.money - int(cost))

    def money_increase(self, cost):
        self.money = self.money + int(cost)
