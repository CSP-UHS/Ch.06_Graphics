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

arcade.open_window(500,400, "Nellie Leaverton")

arcade.set_background_color(arcade.color.WHITE) #set backround color

arcade.start_render()
###############
arcade.draw_circle_filled(240,200, 190, arcade.color.BLACK)

arcade.draw_circle_outline(240,200, 130, arcade.color.ALABAMA_CRIMSON,3)

my_list = ((220, 200),
           (160, 300),
           (320, 300),
           (260, 200),
           (320, 100),
           (160, 100))
arcade.draw_polygon_filled(my_list, arcade.color.ALABAMA_CRIMSON)
###############
arcade.finish_render()

arcade.run()
