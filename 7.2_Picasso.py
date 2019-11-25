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
arcade.open_window(500,400,"My Picasso Picture")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
arcade.draw_circle_filled(250,220,100,arcade.color.YELLOW)
arcade.draw_circle_filled(210,250,5,arcade.color.BLACK)
arcade.draw_circle_filled(290,250,5,arcade.color.BLACK)
arcade.draw_arc_outline(250,170,100,40,arcade.color.BLACK,180,360)
x_offset=180
for i in range(8):
    arcade.draw_line(x_offset,170,x_offset,190,arcade.color.BLACK)
    x_offset+=20

arcade.finish_render()
arcade.run()

