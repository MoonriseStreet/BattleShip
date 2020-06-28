import arcade
from views.MainView import MainView


def main():
    game = MainView()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
