'''
PICASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade
arcade.open_window(300, 300, "Caps Sheild - Emma Moritz")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

point_list=((150,130),
            (130,140),
            (130,165),
            (170,165),
            (170,140))

for x in range(0,300,20):
    arcade.draw_line(0 + x, 0, 0 + x, 300, arcade.color.NAVY_BLUE, 5)
for y in range(0, 300, 20):
    arcade.draw_line(0, 0 + y, 300, 0 + y, arcade.color.NAVY_BLUE, 5)
arcade.draw_circle_filled(150,150,125,(255,0,0))
arcade.draw_circle_filled(150,150,100,(255,255,255))
arcade.draw_circle_filled(150,150,75,(255,0,0))
arcade.draw_circle_filled(150,150,50,(0,0,255))
arcade.draw_triangle_filled(135,165,150,200,165,165,(255,255,255))
arcade.draw_triangle_filled(105,165,130,165,130,140,(255,255,255))
arcade.draw_triangle_filled(195,165,170,165,170,135,(255,255,255))
arcade.draw_triangle_filled(150,130,180,115,170,150,(255,255,255))
arcade.draw_triangle_filled(150,130,120,115,130,150,(255,255,255))
arcade.draw_polygon_filled(point_list,(255,255,255))

arcade.finish_render()
arcade.run()



