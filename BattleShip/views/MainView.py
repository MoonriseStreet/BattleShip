import arcade
from arcade.gui import *
import const
from Button import Button
from Base import Base
from DialogBox import DialogBox
from builder.UnitBuilder import UnitBuilder
from builder.FrigateUnitBuilder import FrigateUnitBuilder
from builder.CruiserUnitBuilder import CruiserUnitBuilder
from builder.BoatUnitBuilder import BoatUnitBuilder
from Player import Player
from Explosion import Explosion


class MainView(arcade.Window):

    def __init__(self):
        super().__init__(const.SCREEN_WIDTH, const.SCREEN_HEIGHT,
                         const.SCREEN_TITLE)

        self.background = None
        self.time = 0
        self.last_click = -1
        self.last_start = -1
        self.explosion_texture = arcade.load_texture("pic/explosion.png")

        self.player = Player()
        self.dialog_box = DialogBox()
        self.player_base = None
        self.enemy_base = None
        self.player_ships = None
        self.enemy_ships = None
        self.explosions_list = None

    def set_buttons(self):
        for i in range(const.SHIPS_COUNT):
            button = Button(const.BUTTON_X, const.BUTTON_Y[i],
                            const.BUTTON_WIDTH[i], const.BUTTON_HEIGHT,
                            const.SHIPS_NAME[i] + '\n' + str(
                                const.SHIPS_COST[i]) + '$',
                            const.SHIPS_NAME[i], 17)
            button.cost = const.SHIPS_COST[i]
            self.button_list.append(button)
        self.button_list.append(self.dialog_box.supply_button)
        self.button_list.append(self.dialog_box.weapon_button)
        self.button_list.append(self.dialog_box.go_button)


    def setup(self):
        self.background = arcade.load_texture(const.MAIN_PIC)
        self.set_buttons()
        self.player_ships = arcade.SpriteList()
        self.enemy_ships = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()

        self.player_base = Base(const.BASE1_POSITION_X, const.BASE1_POSITION_Y,
                                const.BAR1_POSITION_X, const.BAR1_POSITION_Y)
        self.enemy_base = Base(const.BASE2_POSITION_X, const.BASE2_POSITION_Y,
                               const.BAR2_POSITION_X, const.BAR2_POSITION_Y)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, const.SCREEN_WIDTH,
                                            const.SCREEN_HEIGHT, self.background)
        super().on_draw()
        self.player.draw()
        self.explosions_list.draw()
        self.player_ships.draw()
        self.enemy_ships.draw()
        self.player_base.draw()
        self.enemy_base.draw()
        self.dialog_box.draw()

    def clone(self, number: int):
        self.player.set_builder(number)
        fighter = self.player.clone()
        if self.player.money < fighter.cost:
            return
        fighter.center_x = const.PLAYER_LOCATION_X
        fighter.center_y = const.PLAYER_LOCATION_Y
        fighter.change_x = const.FIGHTERS_SPEED
        fighter.side = 'player'
        self.player_ships.append(fighter)
        self.player.money_decrease(fighter.cost)

    def lock_buttons(self, button):
        button.locked = True
        self.last_click = self.time

    def on_update(self, delta_time):
        self.explosions_list.update()
        self.player_base.update()
        self.enemy_base.update()
        self.player_ships.update()
        self.enemy_ships.update()
        self.check_ships(self.player_ships)
        self.check_ships(self.enemy_ships)
        self.check_collisions(self.player_ships, self.enemy_base)
        self.check_collisions(self.enemy_ships, self.player_base)
        for i in range(const.SHIPS_COUNT):
            if self.button_list[i].pressed:
                self.dialog_box.curr = i
                self.dialog_box.update()
        if self.dialog_box.supply_button.pressed and self.time > self.last_click + 20 * delta_time:
            self.last_click = self.time
            self.dialog_box.supply_button.checked = not self.dialog_box.supply_button.checked
        if self.dialog_box.weapon_button.pressed and self.time > self.last_click + 20 * delta_time:
            self.last_click = self.time
            self.dialog_box.weapon_button.checked = not self.dialog_box.weapon_button.checked
        if self.dialog_box.go_button.pressed and not self.dialog_box.go_button.checked:
            self.clone(self.dialog_box.curr)
            self.dialog_box.go_button.checked = True
            self.dialog_box.supply_button.checked = False
            self.dialog_box.weapon_button.checked = False
            self.last_start = self.time
        if self.time > self.last_start + const.BUTTON_DELAY:
            self.dialog_box.go_button.checked = False
        if const.SHIPS_COST[self.dialog_box.curr] > self.player.money:
            self.dialog_box.go_button.locked = True
        if const.EXTRA_SUPPLY_COST > self.player.money:
            self.dialog_box.supply_button.locked = True
        if const.EXTRA_WEAPON_COST > self.player.money:
            self.dialog_box.weapon_button.locked = True
        self.time += delta_time

    def check_collisions(self, ships, base):
        for ship in ships:
            if arcade.check_for_collision(ship, base):
                base.damage(ship.make_damage())
                explosion = Explosion(self.explosion_texture)
                explosion.center_x = base.center_x
                explosion.center_y = base.center_y
                explosion.update()
                self.explosions_list.append(explosion)
                ship.remove_from_sprite_lists()

    def check_ships(self, ships):
        for ship in ships:
            if ship.get_hp() <= 0:
                explosion = Explosion(ship.dying_sprite)
                explosion.center_x = ship.center_x
                explosion.center_y = ship.center_y
                explosion.update()
                self.explosions_list.append(explosion)
                ship.remove_from_sprite_lists()
