from arcade import View, start_render, load_texture, draw_text, color, draw_lrwh_rectangle_textured
from const import (ANOTHER_PIC, SCREEN_WIDTH, SCREEN_HEIGHT, TEXT_POS_X, TEXT_POS_Y,
                   FONT_NAME, FONT_SIZE, TEXT_WIN, BUTTON_POS_X, BUTTON_POS_Y, BUTTON_MESSAGE,
                   RESULT_BUTTON_WIDTH, RESULT_BUTTON_HEIGHT)
from Button import Button
import views.MainView


class WinView(View):
    def __init__(self):
        super().__init__()
        self.background = load_texture(ANOTHER_PIC)
        button = Button(BUTTON_POS_X, BUTTON_POS_Y, RESULT_BUTTON_WIDTH, RESULT_BUTTON_HEIGHT,
                             BUTTON_MESSAGE, "", FONT_SIZE)
        self.button_list.append(button)

    def on_draw(self):
        start_render()
        draw_lrwh_rectangle_textured(0, 0,
                                     SCREEN_WIDTH, SCREEN_HEIGHT,
                                     self.background)
        draw_text(TEXT_WIN, TEXT_POS_X, TEXT_POS_Y, color.COOL_BLACK,
                  FONT_SIZE, font_name=FONT_NAME)
        for button in self.button_list:
            button.draw()

    def on_update(self, delta_time):
        for button in self.button_list:
            if button.pressed:
                game = views.MainView.MainView()
                self.window.show_view(game)