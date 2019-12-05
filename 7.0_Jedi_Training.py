#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade

arcade.open_window(500,500, "jedi training")
arcade.set_background_color(arcade.color.STAR_COMMAND_BLUE)

arcade.start_render()

arcade.draw_rectangle_filled(110,230,45,25, arcade.color.BLUSH)
arcade.finish_render()

arcade.run()
