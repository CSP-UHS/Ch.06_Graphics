'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: dab master aidan kugley

Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500,400, "take home test")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
arcade.draw_rectangle_filled(10,10,20,20,arcade.color.WHITE)

arcade.finish_render()
arcade.run()