#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
25 across 20 down
'''

import arcade
arcade.open_window(500,400,"Yoda's species is called Yoda's Species")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

h=20
xvalue=20
for z in range(25):
    arcade.draw_line(xvalue,400,xvalue,0,arcade.color.BLACK,1)
    xvalue+=20
for z in range(25):
    arcade.draw_line(500,h,0,h,arcade.color.BLACK)
    h+=20
arcade.draw_xywh_rectangle_filled(20,360,60,20,arcade.color.PHLOX)
arcade.draw_rectangle_filled(200,280,40,20,arcade.color.BLUSH,45)
arcade.draw_circle_filled(250,220,40,arcade.color.WISTERIA)
arcade.draw_line(80,20,120,60,arcade.color.BLUE,1)
arcade.draw_ellipse_filled(100,100,60,20,arcade.color.AMBER,0,128)
arcade.draw_text("I love you. I know.",20,180,arcade.color.BRICK_RED,20,220,"left","Calibri",False,False,"left","baseline",0)
arcade.finish_render()
arcade.run()