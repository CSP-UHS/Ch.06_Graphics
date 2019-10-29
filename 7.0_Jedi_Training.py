#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade

arcade.open_window(500,400, "Hello")

arcade.set_background_color(arcade.color.ALMOND) #set backround color

arcade.start_render()
#draw in here

#fence posts
for x_offset in range(0,610,20):
    arcade.draw_rectangle_filled(0+x_offset,60,1,700,arcade.color.BLACK)
for y_offset in range(0, 700, 20):
    arcade.draw_rectangle_filled(0+y_offset, 70, 600, 1, arcade.color.BLACK)
    arcade.draw_rectangle_filled(0+y_offset, 52, 600, 1, arcade.color.BLACK)
#draw in here
arcade.finish_render()

arcade.run()
