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
arcade.open_window(425,585, "HELLO")
arcade.set_background_color(arcade.color.GRANNY_SMITH_APPLE)
arcade.start_render()
arcade.draw_rectangle_filled(107.5,55,205,100,arcade.color.WHITE)
arcade.draw_rectangle_filled(265,55,100,100,arcade.color.WHITE)
for x_offset in range(55,266,105):
    arcade.draw_rectangle_filled(x_offset,160,100,100,arcade.color.WHITE)
for x_offset in range(55, 371, 105):
    arcade.draw_rectangle_filled(x_offset,265,100,100,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x_offset,370,100,100,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x_offset,475,100,100,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x_offset,555,100,50,arcade.color.WHITE)
arcade.draw_rectangle_filled(370,107.5,100,205,arcade.color.WHITE)
arcade.finish_render()
arcade.run()











