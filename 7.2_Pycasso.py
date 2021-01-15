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

arcade.open_window(1000,600, "Ethan Januszewski")
arcade.set_background_color(arcade.color.ARSENIC)

arcade.start_render()

for i in range(1000):
    arcade.draw_line(0, i*10, 1000, i*10, arcade.color.BLACK, 2)
    arcade.draw_line(i*10,0 , i*10,1000 , arcade.color.BLACK, 2)

arcade.draw_circle_filled(500,300,325,arcade.color.CHARCOAL)

arcade.draw_line(450,200,600,200,arcade.color.AERO_BLUE,3)
arcade.draw_line(600,200,500,425,arcade.color.AERO_BLUE,3)
arcade.draw_line(500,425,375,100,arcade.color.AERO_BLUE,3)
arcade.draw_line(375,100,250,100,arcade.color.AERO_BLUE,3)
arcade.draw_line(250,100,425,550,arcade.color.AERO_BLUE,3)
arcade.draw_line(425,550,575,550,arcade.color.AERO_BLUE,3)
arcade.draw_line(575,550,750,100,arcade.color.AERO_BLUE,3)
arcade.draw_line(750,100,525,100,arcade.color.AERO_BLUE,3)
arcade.draw_line(525,100,450,200,arcade.color.AERO_BLUE,3)

arcade.finish_render()

arcade.run()
