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



import random
import arcade
arcade.open_window(600, 600, "Pycasso Project, Bryce Getz")
arcade.set_background_color((0, 150, 255))
arcade.start_render()




arcade.draw_lrtb_rectangle_filled(200, 400, 500, 0, (0, 0, 0)) #Back drop for the building


for y in range (0, 505, 10): #horizontal levels
    arcade.draw_rectangle_filled(300, y, 200, 5, (255, 255, 255))

for x in range (200, 405, 10):#VERTICAL LINES
    arcade.draw_rectangle_filled(x, 250, 5, 500, (255, 255, 255))


arcade.draw_lrtb_rectangle_filled(0, 600, 10, 0, (0, 200, 0))

for x in range (0, 600, 3):#GRASS 1
    top=random.randint(-3,3)
    top2=random.randint(10,13,)
    arcade.draw_line(x, 0,x+top,top2,(0,100,0))

for x in range (0, 600, 3):#GRASS 2
    top=random.randint(-3,3)
    top2=random.randint(10,13,)
    arcade.draw_line(x, 0,x+top,top2,(0,150,0))

arcade.draw_circle_filled(500, 500, 75, (255, 255, 0))


arcade.finish_render()

arcade.run()
