'''
PYCASSO PROJECT
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

arcade.open_window(500, 500, "Tom Dau")                                 # Discord Logo

arcade.start_render()

arcade.draw_circle_filled(250, 250, 210, (255, 255, 255))               # White Border
arcade.draw_circle_filled(250, 250, 200, (114, 137, 217))               # Blue Circle

point_list = ((125,185),                                                # White outline
              (175,150),
              (325,150),
              (375,185),
              (350,325),
              (275,350),
              (225,350),
              (150,325))
arcade.draw_polygon_filled(point_list, (255, 255, 255))

arcade.draw_ellipse_filled(250, 250, 200, 200, (114, 137, 217))         # Blue overlap to shape
arcade.draw_ellipse_filled(250, 350, 100, 150, (114, 137, 217))         # ^^^
arcade.draw_ellipse_filled(250, 125, 125, 100, (114, 137, 217))         # ^^^
arcade.draw_ellipse_filled(250, 250, 215, 175, (255, 255, 255))         # White overlap to shape

for eye in range(150, 275, 75):                                         # Eye loop
    arcade.draw_circle_filled(63+eye, 235, 25, (114, 137, 217))
arcade.finish_render()

arcade.run()