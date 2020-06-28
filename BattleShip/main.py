from arcade import Window, run
from views.MainView import MainView
from views.WinView import WinView
from views.DefeatView import DefeatView
from const import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game = MainView()
    window.show_view(game)
    run()


if __name__ == "__main__":
    main()
