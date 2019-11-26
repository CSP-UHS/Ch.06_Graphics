#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade
arcade.open_window(500, 400, "Test")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
x_offset=0
for i in range(25):
    arcade.draw_line(x_offset,0,x_offset,400,arcade.color.WHITE)
    x_offset+=20
y_offset=0
for i in range(20):
    arcade.draw_line(0,y_offset,500,y_offset,arcade.color.WHITE)
    y_offset+=20
arcade.draw_circle_filled(250,250,80,arcade.color.ASH_GREY)
arcade.draw_rectangle_filled(250,160,160,195,arcade.color.WHITE)
arcade.draw_rectangle_filled(190,53,40,23,arcade.color.WHITE)
arcade.draw_line(170,40,160,20,arcade.color.WHITE,5)
arcade.draw_rectangle_filled(250,310,20,40,arcade.color.DARK_BLUE)
arcade.draw_circle_filled(250,310,10,arcade.color.CHARTREUSE)
arcade.draw_rectangle_filled(195,280,20,30,arcade.color.DARK_BLUE)
arcade.draw_ellipse_filled(230,280,10,15,arcade.color.DARK_BLUE)
arcade.draw_ellipse_filled(270,275,20,15,arcade.color.DARK_BLUE)
arcade.draw_circle_filled(270,275,10,arcade.color.RED)
arcade.draw_rectangle_filled(250,260,160,10,arcade.color.DARK_BLUE)
arcade.draw_rectangle_filled(305,280,20,30,arcade.color.DARK_BLUE)
arcade.draw_rectangle_filled(250,65,160,10,arcade.color.DARK_BLUE)
# arcade.draw_circle_filled()
y_offset=245
for i in range (3):
    arcade.draw_rectangle_filled(250,y_offset,80,10,arcade.color.DARK_BLUE)
    y_offset-=20
arcade.draw_ellipse_filled(210,150,10,40,arcade.color.DARK_BLUE)
arcade.finish_render()
arcade.run()