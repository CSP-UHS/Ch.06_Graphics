#Sign your name: Geni Williams

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500, 400,"Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
arcade.draw_line(0, 5, 5, 0, arcade.color.BLACK, 2)

arcade.finish_render()
arcade.run()