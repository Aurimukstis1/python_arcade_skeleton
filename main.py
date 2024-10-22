import arcade

# display settings
WIDTH, HEIGHT = 1280, 720
SCREEN_SIZE = (WIDTH, HEIGHT)


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.enable_timings(100)
        self.mouse_x = 0
        self.mouse_y = 0

    def on_update(self, dt):
        pass

    def on_draw(self):
        self.clear()

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def cleanup(self):
        pass


def main():
    game = Game(WIDTH, HEIGHT, "arcade project")
    arcade.run()
    game.cleanup()


if __name__ == "__main__":
    main()