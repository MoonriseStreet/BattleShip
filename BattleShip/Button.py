from arcade.gui import *
import const


class Button(TextButton):
    def __init__(self, x, y, width, height, text, name, font_size):
        theme = Theme()
        theme.set_font(font_size, arcade.color.COOL_BLACK, font_name=const.FONT_NAME)
        theme.add_button_textures(const.EMPTY_PIC)
        super().__init__(x, y, width, height,
                         text, theme=theme)
        self.cost = None
        self.name = name
        self.pressed = False
        self.checked = False
        self.locked = False

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False

    def draw_texture_theme(self):
        if self.locked:
            arcade.draw_texture_rectangle(self.center_x, self.center_y,
                                          self.width, self.height,
                                          self.clicked_texture)
        else:
            arcade.draw_texture_rectangle(self.center_x, self.center_y,
                                          self.width, self.height,
                                          self.normal_texture)
