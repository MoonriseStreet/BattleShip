# SCREEN PARAMETERS

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "BattleShip"

# FIGHTERS PARAMETERS

FIGHTERS_SPEED = 1.25

PLAYER_LOCATION_X = 120
PLAYER_LOCATION_Y = 400

ENEMY_LOCATION_X = 680
ENEMY_LOCATION_Y = 400

# SHIPS_PARAMETERS

SHIPS_COUNT = 3
SHIPS_NAME = ["boat", "frigate", "cruiser"]
SHIPS_IMAGE = [
    ["pic/boat.png", "pic/dying_boat.png"],
    ["pic/frigate.png", "pic/dying_frigate.png"],
    ["pic/cruiser.png", "pic/dying_cruiser.png"]
]
SHIPS_COST = [100, 200, 500]
SHIPS_HP = [1000, 3000, 10000]
SHIPS_DAMAGE = [150, 200, 500]
SHIPS_BLOW_DAMAGE = [50, 50, 100]
SHIPS_CONSUMPTION = [1400, 2000, 4000]

# BUTTONS_PARAMETERS

BUTTON_X = 105
BUTTON_Y = [248, 165, 75]
BUTTON_WIDTH = [60, 90, 90]
BUTTON_HEIGHT = 35
BUTTON_DELAY = 1.5
TIME_DELAY = 20
BUTTON_FONT_SIZE = 17
BUTTON_FONT_SIZE_L = 18
BUTTON_FONT_SIZE_XL = 20

# BASES PARAMETERS

PLAYER_BASE_POSITION_X = 100
PLAYER_BASE_POSITION_Y = 400

ENEMY_BASE_POSITION_X = 700
ENEMY_BASE_POSITION_Y = 400

MAX_BASE_HP = 500

# HEALTHBAR PARAMETERS

PLAYER_BAR_POSITION_X = 144
PLAYER_BAR_POSITION_Y = 326

ENEMY_BAR_POSITION_X = 660
ENEMY_BAR_POSITION_Y = 320

BAR_LENGTH = 130
BAR_HEIGHT = 18

# DIALOG WINDOW PARAMETERS

PICTURE_X = 290
PICTURE_Y = 160
PICTURE_SIZE = [
    (80, 76), (108, 66), (135, 94)
]

TITLE_X = 260
TITLE_Y = 77

SUPPLY_X = 465
SUPPLY_Y = 190

WEAPON_X = 465
WEAPON_Y = 130

GO_X = 465
GO_Y = 70

DIALOG_BUTTON_WIDTH = 160
DIALOG_BUTTON_HEIGHT = 50

EXTRA_SUPPLY_COST = 20
EXTRA_WEAPON_COST = 20

WEAPON_COEFFICIENT = 1.2
SUPPLY_COEFFICIENT = 1.4
CONSUMPTION_COEFFICIENT = 1.05


# MONEY BAR

INIT_MONEY = 1000
ENOUGH_MONEY = 200
MONEY_COEFFICIENT = 1000

MONEY_BAR_X = 245
MONEY_BAR_Y = 245
MONEY_FONT_SIZE = 22

II_DIGIT_LENGTH = 80
III_DIGIT_LENGTH = 120
MORE_DIGIT_LENGTH = 160

# RESULT WINDOW

FONT_SIZE = 25
TEXT_POS_X = int(SCREEN_WIDTH / 2 - 60)
TEXT_POS_Y = int(SCREEN_HEIGHT - SCREEN_HEIGHT / 2.5)
TEXT_WIN = "Victory!"
TEXT_DEFEAT = "Defeat!"
BUTTON_POS_X = int(SCREEN_WIDTH / 2)
BUTTON_POS_Y = int(SCREEN_HEIGHT / 2)
RESULT_BUTTON_WIDTH = 200
RESULT_BUTTON_HEIGHT = 60
BUTTON_MESSAGE = "Play again"

# TIME PARAMETERS

PLAYER_IDLE = 15
PLAYER_IDLE_NUMBER = 314159
STRATEGY_UPDATE = 12
FREQUENT = 2
MEDIUM = 3
RARE = 4

# ESTIMATE FORCE CONSTANTS

COST_COEFFICIENT = 500
HP_COEFFICIENT = 1000

# OTHER

EXPLOSION_DURATION = 30

FONT_NAME = 'fonts/KGSecondChancesSolid.ttf'
MAIN_PIC = 'pic/mainView.png'
ANOTHER_PIC = 'pic/anotherView.png'
EMPTY_PIC = 'pic/empty.png'
EXPLOSION_PIC = 'pic/explosion.png'
