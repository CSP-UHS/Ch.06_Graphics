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



arcade.draw_xywh_rectangle_filled(20,362,58,18,arcade.color.PHLOX) #Top left purple rectangle

arcade.draw_arc_filled(405,320,60,60,arcade.color.YELLOW,30,330,0) #Pacman

arcade.draw_rectangle_filled(196,265,40,20,arcade.color.BLUSH,45) #Pink angled rectangle

arcade.draw_circle_filled(250,211,40,arcade.color.WISTERIA) #Middle Circle light purple

arcade.draw_text("I live you.I know.",20,170,arcade.color.BRICK_RED,20,220,"left","Calibri", False,False,"left","baseline" ,0) #Textbox

arcade.draw_ellipse_filled(98,96,60,20,arcade.color.AMBER,0,128) #Bottom left elipse

arcade.draw_line(77,17,118,58,arcade.color.BLUE,1)

arcade.draw_rectangle_filled(462,10,5,5,arcade.color.RED,0) #Bottom right small rectangle



arcade.finish_render() #Run Arcade
arcade.run()