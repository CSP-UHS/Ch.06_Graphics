#Sign your name:  Malsawmthara Hmar (Henry)

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade

arcade.open_window(500,400,"Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
x_offset=0
y_offset=0
for i in range(25):
    x_offset+=20
    arcade.draw_line(x_offset,0,x_offset,400,arcade.color.BLACK)  #draw the vertical lines
for i in range(20):
    y_offset+=20
    arcade.draw_line(0,y_offset,500,y_offset,arcade.color.BLACK)  #draw the horizontal lines
arcade.draw_line(80,20,120,60,arcade.color.BLUE) #draw the blue line
arcade.draw_ellipse_filled(100,100,60,20,arcade.color.AMBER)    # drawing the amber oval at the bottom
arcade.draw_rectangle_filled(50,370,60,20,arcade.color.PHLOX)   # draw the pink rectangle
arcade.draw_rectangle_filled(200,260,40,20,arcade.color.BLUSH,45) # rotated rectangle
arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA) # circle in the middle
arcade.draw_text("I love you. I know.", 21, 160, arcade.color.BRICK_RED, 20) # the text
arcade.draw_rectangle_filled(460,10,5,5,arcade.color.RED) #little red dot
arcade.draw_arc_filled(400,320,60,60,arcade.color.YELLOW,29,330,0) # yellow arc
arcade.finish_render()
arcade.run()