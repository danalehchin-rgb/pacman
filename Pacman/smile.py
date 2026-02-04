import arcade

TILE_SIZE = 40
SCREEN_TITLE = "Emoji"
def smiley(column, row):
    center_x = (column * TILE_SIZE) + (TILE_SIZE / 2)
    center_y = (row * TILE_SIZE) + (TILE_SIZE / 2)
    arcade.draw_circle_filled(center_x, center_y, 55, arcade.color.PINK)
    eye_offset_x = 8
    eye_offset_y = 8
    eye_radius = 4
    arcade.draw_circle_filled(center_x - eye_offset_x, center_y + eye_offset_y, eye_radius, arcade.color.BLACK)
    arcade.draw_circle_filled(center_x + eye_offset_x, center_y + eye_offset_y, eye_radius, arcade.color.BLACK)
    arcade.draw_arc_outline(center_x, center_y - 2, 20, 10, arcade.color.BLACK, 190, 350, 2)

def main():
    arcade.open_window(800, 600, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    smiley(9, 8)
    arcade.finish_render()
    arcade.run()
main()