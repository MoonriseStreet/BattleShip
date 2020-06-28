from const import (SHIPS_IMAGE, SHIPS_NAME, SUPPLY_X, SUPPLY_Y, DIALOG_BUTTON_WIDTH, DIALOG_BUTTON_HEIGHT,
                   EXTRA_SUPPLY_COST, WEAPON_X, WEAPON_Y, EXTRA_WEAPON_COST, GO_X, GO_Y, PICTURE_X, PICTURE_Y,
                   PICTURE_SIZE, TITLE_X, TITLE_Y, FONT_NAME, BUTTON_FONT_SIZE_L, BUTTON_FONT_SIZE_XL)
from arcade import load_texture, draw_texture_rectangle, draw_text, color
from Button import Button


class DialogBox(object):
    def __init__(self):
        self.curr = 0
        self.name = None
        self.texture = load_texture(SHIPS_IMAGE[self.curr][0])
        self.title = SHIPS_NAME[self.curr]
        self.supply_button = Button(SUPPLY_X, SUPPLY_Y, DIALOG_BUTTON_WIDTH, DIALOG_BUTTON_HEIGHT,
                                    '+supply\t' + str(EXTRA_SUPPLY_COST) + '$', 'supply', BUTTON_FONT_SIZE_L)
        self.weapon_button = Button(WEAPON_X, WEAPON_Y,
                                    DIALOG_BUTTON_WIDTH, DIALOG_BUTTON_HEIGHT,
                                    '+weapon\t' + str(EXTRA_WEAPON_COST) + '$', 'weapon', BUTTON_FONT_SIZE_L)
        self.go_button = Button(GO_X, GO_Y, DIALOG_BUTTON_WIDTH, DIALOG_BUTTON_HEIGHT, 'GO!', 'go', BUTTON_FONT_SIZE_XL)

    def update(self):
        self.reset_button(self.weapon_button)
        self.reset_button(self.supply_button)
        self.reset_button(self.go_button)
        self.name = SHIPS_NAME[self.curr]
        self.texture = load_texture(SHIPS_IMAGE[self.curr][0])
        self.title = SHIPS_NAME[self.curr]

    def draw(self):
        draw_texture_rectangle(PICTURE_X, PICTURE_Y, PICTURE_SIZE[self.curr][0],
                               PICTURE_SIZE[self.curr][1], texture=self.texture)
        draw_text(self.title, TITLE_X, TITLE_Y, color.COOL_BLACK,
                  BUTTON_FONT_SIZE_L, font_name=FONT_NAME)
        self.update_button(self.supply_button)
        self.update_button(self.weapon_button)
        self.update_button(self.go_button)

    def update_button(self, button):
        if button.locked:
            button.font_color = color.AUBURN
        elif button.checked:
            button.font_color = color.LAPIS_LAZULI
        else:
            button.font_color = color.COOL_BLACK

    def reset_button(self, button):
        button.checked = False
        button.locked = False
