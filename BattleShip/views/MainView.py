from arcade import (View, load_texture, SpriteList, start_render, draw_lrwh_rectangle_textured,
                    draw_texture_rectangle, color, draw_text
                    )
from const import (MAIN_PIC, SCREEN_WIDTH, SCREEN_HEIGHT,
                   BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_DELAY,
                   SHIPS_COUNT, SHIPS_NAME, SHIPS_IMAGE, SHIPS_COST, EXTRA_SUPPLY_COST, EXTRA_WEAPON_COST,
                   PLAYER_LOCATION_X, PLAYER_LOCATION_Y, ENEMY_LOCATION_X, ENEMY_LOCATION_Y, FIGHTERS_SPEED,
                   TIME_DELAY, BUTTON_FONT_SIZE
                   )
from Button import Button
from DialogBox import DialogBox
from decorator.SupplyDecorator import SupplyDecorator
from decorator.WeaponDecorator import WeaponDecorator
from Player import Player
from Enemy import Enemy
from SpriteManager import SpriteManager
from views.DefeatView import DefeatView
from views.WinView import WinView


class MainView(View):

    def __init__(self):
        super().__init__()
        self.time = 0
        self.last_click = -1
        self.last_start = -1

        self.player = Player()
        self.enemy = Enemy()
        self.dialog_box = DialogBox()
        self.background = load_texture(MAIN_PIC)
        self.sprite_manager = SpriteManager()
        self.set_buttons()
        self.sprite_manager.setup()
        self.enemy.setup()

    def set_buttons(self):
        for i in range(SHIPS_COUNT):
            button = Button(BUTTON_X, BUTTON_Y[i], BUTTON_WIDTH[i], BUTTON_HEIGHT,
                            SHIPS_NAME[i] + '\n' + str(SHIPS_COST[i]) + '$', SHIPS_NAME[i], BUTTON_FONT_SIZE)
            self.button_list.append(button)
        self.button_list.append(self.dialog_box.supply_button)
        self.button_list.append(self.dialog_box.weapon_button)
        self.button_list.append(self.dialog_box.go_button)

    def on_draw(self):
        start_render()
        draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        for button in self.button_list:
            button.draw()
        self.dialog_box.draw()
        self.sprite_manager.draw_sprites()
        self.player.draw()

    def on_update(self, delta_time):
        new_ship = self.enemy.on_update(delta_time, self.sprite_manager.game_state())
        if new_ship is not None:
            self.sprite_manager.add_enemy_ship(new_ship)
        self.sprite_manager.update(delta_time)
        self.player.money_increase(self.sprite_manager.player_fight_benefit())
        self.enemy.money_increase(self.sprite_manager.enemy_fight_benefit())
        for i in range(SHIPS_COUNT):
            if self.button_list[i].pressed:
                self.dialog_box.curr = i
                self.dialog_box.update()
        self.update_buttons(delta_time)
        self.time += delta_time

        status = self.sprite_manager.check_end_game()
        if status != 0:
            final_view = DefeatView() if status == 1 else WinView()
            self.window.show_view(final_view)

    def clone(self, number: int):
        self.player.set_builder(number)
        fighter = self.player.clone()
        if self.dialog_box.weapon_button.checked:
            fighter = WeaponDecorator(fighter)
        if self.dialog_box.supply_button.checked:
            fighter = SupplyDecorator(fighter)
        if self.player.money < fighter.get_cost():
            return
        fighter.center_x = PLAYER_LOCATION_X
        fighter.center_y = PLAYER_LOCATION_Y
        fighter.change_x = FIGHTERS_SPEED
        fighter.side = 'player'
        self.sprite_manager.add_ship(fighter)
        self.player.money_decrease(fighter.cost)

    def lock_buttons(self, button):
        button.locked = True
        self.last_click = self.time

    def update_buttons(self, delta_time):
        if self.dialog_box.supply_button.pressed and self.time > self.last_click + TIME_DELAY * delta_time:
            self.last_click = self.time
            self.dialog_box.supply_button.checked = not self.dialog_box.supply_button.checked
        if self.dialog_box.weapon_button.pressed and self.time > self.last_click + TIME_DELAY * delta_time:
            self.last_click = self.time
            self.dialog_box.weapon_button.checked = not self.dialog_box.weapon_button.checked
        if self.dialog_box.go_button.pressed and not self.dialog_box.go_button.checked:
            self.clone(self.dialog_box.curr)
            self.dialog_box.go_button.checked = True
            self.dialog_box.supply_button.checked = False
            self.dialog_box.weapon_button.checked = False
            self.last_start = self.time
        if self.time > self.last_start + BUTTON_DELAY:
            self.dialog_box.go_button.checked = False
        if SHIPS_COST[self.dialog_box.curr] > self.player.money:
            self.dialog_box.go_button.locked = True
        else:
            self.dialog_box.go_button.locked = False

        if SHIPS_COST[self.dialog_box.curr] + EXTRA_SUPPLY_COST > self.player.money or \
                self.dialog_box.weapon_button.checked and \
                SHIPS_COST[self.dialog_box.curr] + EXTRA_WEAPON_COST + EXTRA_SUPPLY_COST > self.player.money:
            self.dialog_box.supply_button.locked = True
        else:
            self.dialog_box.supply_button.locked = False

        if SHIPS_COST[self.dialog_box.curr] + EXTRA_WEAPON_COST > self.player.money or \
                self.dialog_box.supply_button.checked and \
                SHIPS_COST[self.dialog_box.curr] + EXTRA_WEAPON_COST + EXTRA_SUPPLY_COST > self.player.money:
            self.dialog_box.weapon_button.locked = True
        else:
            self.dialog_box.weapon_button.locked = False
