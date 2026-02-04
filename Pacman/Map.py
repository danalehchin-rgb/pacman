import arcade
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Pacman"
TILE_SIZE = 32

LEVEL_MAP = ["WWWWWWWWWWWWWWWWWWWWWWWWW",
    "W P           C         W",
    "W WWWW  WWWWWWWW  WWWW  W",
    "W G        C         G  W",
    "W WWWW  WW  WW  WW  WWWW W",
    "W C     W    W   W     C W",
    "WWWWWWWWWWWWWWWWWWWWWWWWW",]

class Pacman(arcade.Sprite):
    def __init__(self):
        super().__init__()
        # כאן אנחנו טוענים את התמונה החדשה
        self.texture = arcade.load_texture("pacgirl.png")
        self.width = 35
        self.height = 30

class Ghost(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("ghost.png")
        self.width = 35
        self.height = 30

class Coin(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("coins.png")
        self.width = 35
        self.height = 30


class Wall(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.make_soft_square_texture(TILE_SIZE, arcade.color.BLUE, outer_alpha=255)
        self.width = TILE_SIZE
        self.height = TILE_SIZE

class PacmanGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player = None
        self.game_over = False
        self.background_color = arcade.color.BLACK
        self.start_x = 0
        self.start_y = 0

    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.game_over = False
        rows = len(LEVEL_MAP)
        for row_idx, row in enumerate(LEVEL_MAP):
            for col_idx, cell in enumerate(row):
                x = col_idx * TILE_SIZE + TILE_SIZE / 2
                y = (rows - row_idx - 1) * TILE_SIZE + TILE_SIZE / 2
                if cell == 'W':
                    wall = Wall()
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

                elif cell == 'C':
                    coin = Coin()
                    coin.center_x = x
                    coin.center_y = y
                    self.coin_list.append(coin)

                elif cell == 'G':  # Ghost
                    ghost = Ghost()
                    ghost.center_x = x
                    ghost.center_y = y
                    self.ghost_list.append(ghost)

                elif cell == 'P':  # Player (Pacman)
                    self.player = Pacman()
                    self.player.center_x = x
                    self.player.center_y = y
                    self.player_list.append(self.player)
                    self.start_x = x
                    self.start_y = y

    def on_draw(self):

        self.wall_list.draw()
        self.ghost_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        arcade.draw_text("Score: 0", 10, self.window.height - 20, arcade.color.WHITE, 14)
        arcade.draw_text("Lives: 3", 10, self.window.height - 40, arcade.color.WHITE, 14)

        if self.game_over:
            arcade.draw_text("GAME OVER", self.window.width / 2, self.window.height / 2,
                             arcade.color.RED, 30, anchor_x="center")

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        pass

    def collision(self):
        pass

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game_view = PacmanGame()
    game_view.setup()
    window.show_view(game_view)
    arcade.run()
    #test
main()