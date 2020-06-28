import arcade
from arcade.gui import *
import const
from Button import Button
from builder.UnitBuilder import UnitBuilder
from builder.DestroyerUnitBuilder import DestroyerUnitBuilder
from builder.CruiserUnitBuilder import CruiserUnitBuilder
from builder.BoatUnitBuilder import BoatUnitBuilder
from Player import Player
from Explosion import Explosion


class MainView(arcade.Window):

    def __init__(self):
        super().__init__(const.SCREEN_WIDTH, const.SCREEN_HEIGHT, const.SCREEN_TITLE)

        
        self.player = Player()
        self.base1 = None
        self.base2 = None
        self.fighter_list = None
        self.background = None
        self.time = 0
        self.last_click = -1
        self.explosions_list = None
        self.explosion_texture = arcade.load_texture("pic/explosion.png")

    def set_buttons(self):
        for i in range(const.BUTTONS_COUNT):
            normal = const.BUTTON_IMAGES[i][0]
            hover = const.BUTTON_IMAGES[i][1]
            clicked = const.BUTTON_IMAGES[i][1]
            locked = const.BUTTON_IMAGES[i][1]
            theme = Theme()
            theme.add_button_textures(normal, hover, clicked, locked)
            self.button_list.append(Button(self, const.BUTTON_NAME[i],
                                           const.BUTTON_X, const.BUTTON_Y[i], const.BUTTON_WIDTH[i], theme=theme))

    def setup(self):
        self.background = arcade.load_texture("pic/mainView.png")
        self.fighter_list = arcade.SpriteList()
        self.set_buttons()
        self.explosions_list = arcade.SpriteList()
        self.base2 = arcade.Sprite()
        self.base2.set_hit_box([[1, 1], [-1, 1], [-1, -1], [1, -1]])
        self.base2.center_x = const.BASE1_POSITION_X
        self.base2.center_y = const.BASE1_POSITION_Y

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, const.SCREEN_WIDTH,
                                            const.SCREEN_HEIGHT, self.background)
        super().on_draw()
        self.explosions_list.draw()
        self.fighter_list.draw()

    def clone(self, type: str):
        if type == "destroyer":
            unit_builder: UnitBuilder = DestroyerUnitBuilder()
        elif type == "cruiser":
            unit_builder: UnitBuilder = CruiserUnitBuilder()
        else:
            unit_builder: UnitBuilder = BoatUnitBuilder()

        self.player.set_builder(unit_builder)
        fighter = self.player.clone().fighter

        fighter.center_x = const.PLAYER_LOCATION_X
        fighter.center_y = const.PLAYER_LOCATION_Y
        fighter.change_x = const.FIGHTERS_SPEED
        self.fighter_list.append(fighter)

    def lock_buttons(self):
        for button in self.button_list:
            button.locked = True
        self.last_click = self.time

    def unlock_buttons(self):
        for button in self.button_list:
            button.locked = False

    def on_update(self, delta_time):
        self.explosions_list.update()
        self.base2.update()
        self.fighter_list.update()
        for ship in self.fighter_list:
            if arcade.check_for_collision(ship, self.base2):
                explosion = Explosion(self.explosion_texture)
                explosion.center_x = self.base2.center_x
                explosion.center_y = self.base2.center_y
                explosion.update()
                self.explosions_list.append(explosion)
                ship.remove_from_sprite_lists()
        for button in self.button_list:
            if button.pressed and not button.locked:
                self.clone(button.type)
                self.lock_buttons()
                break
        self.time += delta_time
        if self.time > self.last_click + const.BUTTON_DELAY:
            self.unlock_buttons()
