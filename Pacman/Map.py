import arcade
import random

WINDOW_WIDTH = 928
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Pacman"
TILE_SIZE = 32

LEVEL_MAP = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W  P C C C W W W C C C CCC  W",
    "W  WWWWW C W W W C WWWWWW C W",
    "W  CGC C C C C C C C C CC C W",
    "W  WWW C WWWWWWWWW C WWWW C W",
    "W  C C C C C G C C C C C    W",
    "W CWWW C WWW   WWW C  WWW   W",
    "W CC C C W G   G W C C CCG  W",
    "W  WWWWW W WWWWW W  WWWWWW  W",
    "W  C CGC C C C C C CC C C C W",
    "W CWWWWW C WWWWW C  WWWWW   W",
    "W GC C C C C C C C CC C C   W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]


class Pacman(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("pacgirl.png")
        self.width = 26
        self.height = 26
        self.change_x = 0
        self.change_y = 0


class Ghost(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("ghost.png")
        self.width = 26
        self.height = 26
        self.change_x = 0
        self.change_y = 0


class Coin(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("coins.png")
        self.width = 20
        self.height = 20


class Wall(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.make_soft_square_texture(TILE_SIZE, arcade.color.BLUE, outer_alpha=255)
        self.width = TILE_SIZE
        self.height = TILE_SIZE


#יצירת המשחק
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
        self.score = 0

    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.game_over = False
        self.score = 0

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

                elif cell == 'G':
                    ghost = Ghost()
                    ghost.center_x = x
                    ghost.center_y = y
                    # מהירות לרוח
                    ghost.change_x = 2
                    ghost.change_y = 0
                    self.ghost_list.append(ghost)

                elif cell == 'P':
                    self.player = Pacman()
                    self.player.center_x = x
                    self.player.center_y = y
                    self.player_list.append(self.player)

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.ghost_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # הצגת הניקוד
        arcade.draw_text(f"Score: {self.score}", 10, self.window.height - 20, arcade.color.WHITE, 14)
        if self.game_over:
            arcade.draw_text("GAME OVER", self.window.width / 2, self.window.height / 2,
                             arcade.color.RED, 30, anchor_x="center")

    def on_update(self, delta_time):
        if self.game_over:
            return

        # תזוזה לרוח
        self.player.center_x += self.player.change_x
        self.player.center_y += self.player.change_y

        # בדיקת התנגשות פקמן (שונטל) בקיר
        if arcade.check_for_collision_with_list(self.player, self.wall_list):
            self.player.center_x -= self.player.change_x
            self.player.center_y -= self.player.change_y

        # איסוף המטבע
        coins_hit = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coins_hit:
            coin.remove_from_sprite_lists()
            self.score += 10

        # תזוזת הרוח
        for ghost in self.ghost_list:
            ghost.center_x += ghost.change_x
            ghost.center_y += ghost.change_y

            # בדיקת התנגשות רוח בקיר
            if arcade.check_for_collision_with_list(ghost, self.wall_list):
                # 1. חזרה אחורה
                ghost.center_x -= ghost.change_x
                ghost.center_y -= ghost.change_y

                # בחירת כיוון חדש
                direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

                if direction == "UP":
                    ghost.change_x = 0
                    ghost.change_y = 2
                elif direction == "DOWN":
                    ghost.change_x = 0
                    ghost.change_y = -2
                elif direction == "LEFT":
                    ghost.change_x = -2
                    ghost.change_y = 0
                elif direction == "RIGHT":
                    ghost.change_x = 2
                    ghost.change_y = 0

        # בדיקת הפסד לפקמן(שונטל)
        if arcade.check_for_collision_with_list(self.player, self.ghost_list):
            self.game_over = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = 3
            self.player.change_x = 0
        elif key == arcade.key.DOWN:
            self.player.change_y = -3
            self.player.change_x = 0
        elif key == arcade.key.LEFT:
            self.player.change_x = -3
            self.player.change_y = 0
        elif key == arcade.key.RIGHT:
            self.player.change_x = 3
            self.player.change_y = 0

    def on_key_release(self, key, modifiers):
        # עוצר את הפקמן כשעוזבים את המקש
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.change_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game_view = PacmanGame()
    game_view.setup()
    window.show_view(game_view)
    arcade.run()
main()