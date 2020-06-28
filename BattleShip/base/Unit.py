import arcade
from const import *


class Unit(arcade.Sprite):
    def __init__(self, components: list):
        self._components = components
        arcade.Sprite.__init__(self, components[0])
        self.dying_sprite = arcade.load_texture(components[1])
        self.cost = components[2]
        self.max_hp = components[3]
        self.damage = components[4]
        self.blow_damage = components[5]
        self.consumption = components[6]
        self.delta = 0
        self.side = None

    def __repr__(self):
        return self._components

    def make_damage(self):
        if self.get_hp() >= self.blow_damage:
            return self.blow_damage
        else:
            return 0

    def get_hp(self):
        if self.side == 'player':
            lost = int(self.consumption * (self.center_x - PLAYER_LOCATION_X) /
                       (BASE2_POSITION_X - PLAYER_LOCATION_X))
        else:
            lost = int(self.consumption * (self.center_x - ENEMY_LOCATION_X) /
                       (BASE1_POSITION_X - ENEMY_LOCATION_X))

        return self.max_hp - lost + self.delta
