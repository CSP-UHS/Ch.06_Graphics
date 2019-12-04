#Sign your name: Danny Halstead

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade #Setup Arcade
arcade.open_window(500,400, "These Aren’t The Droids You’re Looking For...")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

YValue = 400 #Up and Down Lines
for z in range(22):
    arcade.draw_line(0, YValue, 500, YValue, arcade.color.BLACK, 1)
    YValue -= 19.04

XValue = 0 #Left and Right Lines
for z in range(27):
    arcade.draw_line(XValue, 400, XValue, 0, arcade.color.BLACK, 1)
    XValue += 19.23

#Left off here, add in the obects now. 

arcade.finish_render() #Run Arcade
arcade.run()

#YEEEEEEEEEEEEEEEEEEEET