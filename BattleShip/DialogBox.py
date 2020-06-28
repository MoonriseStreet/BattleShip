from arcade.gui import *
import const
import arcade
from Button import Button


class DialogBox(object):
    def __init__(self):
        self.curr = 0
        self.name = None
        self.texture = arcade.load_texture(const.SHIPS_IMAGE[self.curr][0])
        self.title = const.SHIPS_NAME[self.curr]
        self.supply_button = Button(const.SUPPLY_X, const.SUPPLY_Y,
                                    const.DIALOG_BUTTON_WIDTH, const.DIALOG_BUTTON_HEIGHT,
                                    '+supply\t' + str(const.EXTRA_SUPPLY_COST) + '$', 'supply', 18)
        self.weapon_button = Button(const.WEAPON_X, const.WEAPON_Y,
                                    const.DIALOG_BUTTON_WIDTH, const.DIALOG_BUTTON_HEIGHT,
                                    '+weapon\t' + str(const.EXTRA_WEAPON_COST) + '$', 'weapon', 18)
        self.go_button = Button(const.GO_X, const.GO_Y,
                                const.DIALOG_BUTTON_WIDTH, const.DIALOG_BUTTON_HEIGHT, 'GO!', 'go', 20)

    def update(self):
        self.reset_button(self.weapon_button)
        self.reset_button(self.supply_button)
        self.reset_button(self.go_button)
        self.name = const.SHIPS_NAME[self.curr]
        self.texture = arcade.load_texture(const.SHIPS_IMAGE[self.curr][0])
        self.title = const.SHIPS_NAME[self.curr]

    def draw(self):
        arcade.draw_texture_rectangle(const.PICTURE_X, const.PICTURE_Y, const.PICTURE_SIZE[self.curr][0],
                                      const.PICTURE_SIZE[self.curr][1], texture=self.texture)
        arcade.draw_text(self.title, const.TITLE_X, const.TITLE_Y, arcade.color.COOL_BLACK,
                         18, font_name=const.FONT_NAME)
        self.update_button(self.supply_button)
        self.update_button(self.weapon_button)
        self.update_button(self.go_button)

    def update_button(self, button):
        if button.locked:
            button.font_color = arcade.color.AUBURN
        elif button.checked:
            button.font_color = arcade.color.LAPIS_LAZULI
        else:
            button.font_color = arcade.color.COOL_BLACK

    def reset_button(selfself, button):
        button.checked = False
        button.locked = False