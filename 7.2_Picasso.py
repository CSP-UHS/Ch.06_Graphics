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
arcade.open_window(300,300,"steve")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
arcade.draw_ellipse_filled(150,150,110,70,(0,128,0))
arcade.draw_circle_filled(215,200,40,(0,128,0))
arcade.draw_circle_filled(80,200,40,(0,128,0))
arcade.draw_circle_filled(80,200,20,arcade.color.WHITE)
arcade.draw_circle_filled(215,200,20,arcade.color.WHITE)
arcade.draw_circle_filled(80,200,15,arcade.color.BLACK)
arcade.draw_circle_filled(215,200,15,arcade.color.BLACK)
arcade.draw_ellipse_filled(150,130,80,20,arcade.color.PINK)
arcade.draw_ellipse_filled(150,130,40,10,arcade.color.CANDY_PINK)
arcade.draw_text("Croak",20,60,arcade.color.DARK_GREEN,12,)
arcade.finish_render()
arcade.run()


