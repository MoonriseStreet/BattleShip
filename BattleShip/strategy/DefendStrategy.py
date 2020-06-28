from strategy.Strategy import Strategy
from random import randrange
from const import MEDIUM


class DefendStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.time = 0

    def on_update(self, delta_time, info: list):
        self.time += delta_time
        if self.time >= MEDIUM:
            self.time = 0
            return self.new_unit(info[0])
        return None

    def new_unit(self, money) -> int:
        if int(money) > 0:
            return randrange(100) % 2
        else:
            return 0
