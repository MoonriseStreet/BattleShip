from arcade import TextButton, Theme, color, draw_texture_rectangle
from const import FONT_NAME, EMPTY_PIC


class Button(TextButton):
    def __init__(self, x, y, width, height, text, name, font_size):
        theme = Theme()
        theme.set_font(font_size, color.COOL_BLACK, font_name=FONT_NAME)
        theme.add_button_textures(EMPTY_PIC)
        super().__init__(x, y, width, height,
                         text, theme=theme)
        self.cost = None
        self.name = name
        self.pressed = False
        self.checked = False
        self.locked = False

    def on_press(self):
        if not self.locked:
            self.pressed = True

    def on_release(self):
        self.pressed = False

    def draw_texture_theme(self):
        if self.locked:
            draw_texture_rectangle(self.center_x, self.center_y,
                                   self.width, self.height,
                                   self.clicked_texture)
        else:
            draw_texture_rectangle(self.center_x, self.center_y,
                                   self.width, self.height,
                                   self.normal_texture)
