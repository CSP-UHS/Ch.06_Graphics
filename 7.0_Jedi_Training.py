#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade
arcade.open_window(500, 400, "Ch.7 Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
x_offset=0
for i in range(25):
    arcade.draw_line(x_offset,0,x_offset,400,arcade.color.BLACK)
    x_offset+=20
y_offset=0
for i in range(20):
    arcade.draw_line(0,y_offset,500,y_offset,arcade.color.BLACK)
    y_offset+=20
arcade.draw_rectangle_filled(40,480,60,25,arcade.color.)
arcade.finish_render()
arcade.run()