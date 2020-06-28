import arcade
from const import MAX_BASE_HP, BAR_LENGTH, BAR_HEIGHT


class Base(arcade.Sprite):
    def __init__(self, x: int, y: int, bar_x: int, bar_y: int):
        arcade.Sprite.__init__(self)
        self.set_hit_box([[1, 1], [-1, 1], [-1, -1], [1, -1]])
        self.center_x = x
        self.center_y = y
        self.bar_x = bar_x
        self.bar_y = bar_y

        self.max_hp = MAX_BASE_HP
        self.hp = self.max_hp

    def render_healthbar(self):
        if self.hp <= self.max_hp / 5:
            color = arcade.color.AUBURN
        else:
            color = arcade.color.COOL_BLACK
        length = BAR_LENGTH * self.hp / self.max_hp
        x = self.bar_x - BAR_LENGTH * (1 - self.hp / self.max_hp) / 2
        self.draw_bar(x, color, length)

    def draw_bar(self, x, color, length):
        arcade.draw_rectangle_filled(x, self.bar_y, length,
                                     BAR_HEIGHT, color)
        arcade.draw_circle_filled(x + length / 2, self.bar_y,
                                  BAR_HEIGHT / 2, color)
        arcade.draw_circle_filled(x - length / 2, self.bar_y,
                                  BAR_HEIGHT / 2, color)

    def draw(self):
        self.render_healthbar()

    def damage(self, dm):
        self.hp = max(0, self.hp - dm)
