from arcade import Sprite, SpriteList, check_for_collision, load_texture, check_for_collision_with_list
from Explosion import Explosion
from Base import Base
from const import (PLAYER_BASE_POSITION_X, PLAYER_BASE_POSITION_Y, ENEMY_BASE_POSITION_X, ENEMY_BASE_POSITION_Y,
                   PLAYER_BAR_POSITION_X, PLAYER_BAR_POSITION_Y, ENEMY_BAR_POSITION_X, ENEMY_BAR_POSITION_Y,
                   EXPLOSION_PIC, ENEMY_LOCATION_X, ENEMY_LOCATION_Y, FIGHTERS_SPEED, MONEY_COEFFICIENT, PLAYER_IDLE,
                   PLAYER_IDLE_NUMBER, COST_COEFFICIENT, HP_COEFFICIENT)


class SpriteManager(object):

    def __init__(self):
        self.player_ships = None
        self.enemy_ships = None
        self.player_base = None
        self.enemy_base = None
        self.explosions_list = None
        self.player_benefit = 0
        self.enemy_benefit = 0
        self.player_idle = 0
        self.explosion_texture = load_texture(EXPLOSION_PIC)

    def setup(self):
        self.player_ships = SpriteList()
        self.enemy_ships = SpriteList()
        self.explosions_list = SpriteList()
        self.player_base = Base(PLAYER_BASE_POSITION_X, PLAYER_BASE_POSITION_Y,
                                PLAYER_BAR_POSITION_X, PLAYER_BAR_POSITION_Y)
        self.enemy_base = Base(ENEMY_BASE_POSITION_X, ENEMY_BASE_POSITION_Y,
                               ENEMY_BAR_POSITION_X, ENEMY_BAR_POSITION_Y)

    def draw_sprites(self):
        self.explosions_list.draw()
        self.player_ships.draw()
        self.enemy_ships.draw()
        self.player_base.draw()
        self.enemy_base.draw()

    def add_ship(self, fighter):
        self.player_idle = 0
        self.player_ships.append(fighter)

    def update(self, delta_time):
        self.player_idle += delta_time
        self.explosions_list.update()
        self.player_ships.update()
        self.enemy_ships.update()
        self.player_base.update()
        self.enemy_base.update()
        self.check_ships(self.player_ships)
        self.check_ships(self.enemy_ships)
        self.check_collisions(self.player_ships, self.enemy_base)
        self.check_collisions(self.enemy_ships, self.player_base)
        self.make_fights()

    def player_fight_benefit(self) -> int:
        player_benefit = self.player_benefit
        self.player_benefit = 0
        return player_benefit

    def enemy_fight_benefit(self) -> int:
        enemy_benefit = self.enemy_benefit
        self.enemy_benefit = 0
        return enemy_benefit

    def make_fights(self):
        for player_ship in self.player_ships:
            enemy_ships = check_for_collision_with_list(player_ship, self.enemy_ships)
            for enemy_ship in enemy_ships:
                while player_ship.get_hp() > 0 and enemy_ship.get_hp() > 0:
                    player_ship.get_damage(player_ship.blow_damage + enemy_ship.make_damage())
                    enemy_ship.get_damage(enemy_ship.blow_damage + player_ship.make_damage())
                explosion = Explosion(self.explosion_texture)
                explosion.center_x = (player_ship.center_x + enemy_ship.center_x) / 2
                explosion.center_y = player_ship.center_y
                explosion.update()
                self.explosions_list.append(explosion)
                if player_ship.get_hp() <= 0:
                    player_ship.remove_from_sprite_lists()
                if enemy_ship.get_hp() <= 0:
                    enemy_ship.remove_from_sprite_lists()
                if enemy_ship.get_hp() < player_ship.get_hp():
                    self.player_benefit += (1.5 * MONEY_COEFFICIENT - player_ship.cost) /\
                                           MONEY_COEFFICIENT * enemy_ship.cost
                else:
                    self.enemy_benefit += (1.5 * MONEY_COEFFICIENT - enemy_ship.cost) /\
                                          MONEY_COEFFICIENT * player_ship.cost

    def check_collisions(self, ships, base: Sprite):
        for ship in ships:
            if check_for_collision(ship, base):
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

    def add_enemy_ship(self, ship):
        ship.side = 'enemy'
        ship.center_x = ENEMY_LOCATION_X
        ship.center_y = ENEMY_LOCATION_Y
        ship.change_x = -FIGHTERS_SPEED
        self.enemy_ships.append(ship)

    def game_state(self):
        if self.player_idle > PLAYER_IDLE:
            return PLAYER_IDLE_NUMBER
        diff = self.enemy_base.hp - self.player_base.hp
        return diff + self.estimate_force(self.enemy_ships) - self.estimate_force(self.player_ships)

    def estimate_force(self, ships):
        result = 0
        for ship in ships:
            result += ship.cost / COST_COEFFICIENT + ship.get_hp() / HP_COEFFICIENT
        return result

    def check_end_game(self):
        if self.player_base.hp <= 0:
            return 1
        elif self.enemy_base.hp <= 0:
            return 2
        return 0
