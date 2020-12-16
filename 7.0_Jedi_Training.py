#Sign your name:_Jacob Walters_______________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500,400,"Drawling")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

for xoffset in range(0,400,20):
    arcade.draw_line(0,0+xoffset,500,0+xoffset,arcade.color.BLACK)

for xoffset in range(0,500,20):
    arcade.draw_line(0+xoffset,0,0+xoffset,400,arcade.color.BLACK)

arcade.draw_rectangle_filled(50,370,60,20,arcade.color.PHLOX)

arcade.draw_line(80,20,120,60,arcade.color.BLUE)
arcade.draw_text("I love you. I know",20,155,arcade.color.BRICK_RED,20)

arcade.draw_ellipse_filled(250,200,80,80,arcade.color.WISTERIA)

arcade.draw_ellipse_filled(100,100,120,40,arcade.color.AMBER)

arcade.draw_ellipse_filled(460,10,5,5,arcade.color.RED)

point_list=((195,240),(220,265),(205,280),(180,255))
arcade.draw_polygon_filled(point_list,arcade.color.BLUSH)

arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW,25,335)

arcade.finish_render()
arcade.run()