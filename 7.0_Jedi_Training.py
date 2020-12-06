#Sign your name: Ryan Mullins

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500,400,"Ch. 7 Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
#drawing commands
#grid
for xoffset in range (0,620,20):
    arcade.draw_line(xoffset,400,xoffset,0,(arcade.color.BLACK))
for yoffset in range (0,620,20):
    arcade.draw_line(0,yoffset,500,yoffset,(arcade.color.BLACK))
#pink rectangle
rect_list = ((20,360),(80,360),(80,380),(20,380))
arcade.draw_polygon_filled(rect_list,arcade.color.PHLOX)
#lavender circle
arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA,)
#tiled rectangle
arcade.draw_rectangle_filled(200,260,40,20,arcade.color.BLUSH,135)
#blue line
arcade.draw_line(80,20,120,60,arcade.color.BLUE)
#red dot
arcade.draw_rectangle_filled(460,10,5,5,arcade.color.RED)
#orange oval
arcade.draw_ellipse_filled(100,100,120,40,arcade.color.AMBER)
#text
arcade.draw_text("I love you. I know.",20,154,arcade.color.BRICK_RED,21,)
#pacman
arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW,30,330)


arcade.finish_render()
arcade.run()