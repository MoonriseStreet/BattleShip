import arcade
from const import EXPLOSION_DURATION


class Explosion(arcade.Sprite):

    def __init__(self, texture):
        super().__init__()

        self.texture = texture
        self.counter = 0

    def update(self):
        self.counter += 1
        if self.counter > EXPLOSION_DURATION:
            self.remove_from_sprite_lists()
