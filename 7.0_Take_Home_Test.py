'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________

Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500, 400, "Ch. 7 Take Home Test")
arcade.set_background_color(arcade.color.ALMOND)

arcade.start_render()

for x_line in range(0, 500, 20):  # grid
    arcade.draw_rectangle_filled(0 + x_line, 200, 1, 400, arcade.color.BLACK)
for y_line in range(0, 400, 20):
    arcade.draw_rectangle_filled(250, 0 + y_line, 500, 1, arcade.color.BLACK)

arcade.draw_lrtb_rectangle_filled(19.5, 80, 380, 359.5, arcade.color.PHLOX)  # Phlox Block

arcade.draw_rectangle_filled(200, 260, 39, 20, arcade.color.BLUSH, 45)  # Blush Block

arcade.draw_circle_filled(250, 200, 41, arcade.color.WISTERIA)  # Wisteria Circle

arcade.draw_ellipse_filled(100, 99, 60, 19.5, arcade.color.AMBER)  # Amber Ellipse

arcade.draw_rectangle_filled(460, 10, 5, 5, arcade.color.RED)  # Red Square
arcade.finish_render()

arcade.run()