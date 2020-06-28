from decorator.ReverseDecorator import ReverseDecorator
from Player import Player
from base.Unit import Unit
from strategy.RandomStrategy import RandomStrategy
from strategy.AttackStrategy import AttackStrategy
from strategy.DefendStrategy import DefendStrategy
from strategy.VictoryStrategy import VictoryStrategy
from const import STRATEGY_UPDATE, PLAYER_IDLE_NUMBER


class Enemy(Player):
    def __init__(self):
        super().__init__()
        self.time = 0
        self.info = [0, 0]
        self.strategy = RandomStrategy()

    def setup(self):
        self.strategy = RandomStrategy()

    def update_strategy(self):
        if self.info[1] == PLAYER_IDLE_NUMBER:
            self.strategy = VictoryStrategy()
        elif self.info[1] < 0 and self.info[0] == 0:
            self.strategy = DefendStrategy()
        elif self.info[1] > 0 and self.info[0] > 0:
            self.strategy = AttackStrategy()
        else:
            self.strategy = RandomStrategy()

    def clone(self) -> Unit:
        new_unit = self.builders[self.curr].get_unit()
        self.money_decrease(new_unit.cost)
        return new_unit

    def on_update(self, delta_time, game_state) -> Unit:
        self.time += delta_time
        self.info[0] = self.money
        self.info[1] = game_state
        if self.time >= STRATEGY_UPDATE:
            self.time = 0
            self.update_strategy()
        new_unit = self.strategy.on_update(delta_time, self.info)
        if new_unit is not None:
            self.set_builder(new_unit)
            return ReverseDecorator(self.clone())
        return None
