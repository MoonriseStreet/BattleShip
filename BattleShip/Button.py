from arcade.gui import *

class Button(TextButton):
    def __init__(self, game, type, x=0, y=0, width=100, height=40, text="", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.theme = theme
        self.type = type
        self.game = game
        self.pressed = False
        self.locked = False

    def on_press(self):
        if not self.locked:
            self.pressed = True
            self.locked = True

    def on_release(self):
        self.pressed = False

    def draw_texture_theme(self):
        if self.locked:
            arcade.draw_texture_rectangle(self.center_x, self.center_y, self.width, self.height, self.clicked_texture)
        else:
            arcade.draw_texture_rectangle(self.center_x, self.center_y, self.width, self.height, self.normal_texture)
