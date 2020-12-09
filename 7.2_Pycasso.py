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
arcade.open_window(500, 500, 'Ryan Muetzel')

arcade.set_background_color(arcade.color.BATTLESHIP_GREY)

arcade.start_render()

# #Draw the colored sections
arcade.draw_polygon_filled([(120, 325), (250, 400), (380, 325), (250, 250)], arcade.color.BLUE)
arcade.draw_polygon_filled([(120, 325), (120, 175), (250, 100), (250, 250)], arcade.color.RED)
arcade.draw_polygon_filled([(250, 100), (380, 175), (380, 325), (250, 250)], arcade.color.YELLOW)

# #Make Loops to create the lines between pieces
for i in range(4):  # #Draws the lines for the top of the cube
    arcade.draw_line(120+(43.3*i), 325+(25*i), 250+(43.3*i), 250+(25*i), arcade.color.BLACK, 5)
    arcade.draw_line(120+(43.3*i), 325-(25*i), 250+(43.3*i), 400-(25*i), arcade.color.BLACK, 5)
    # #Draws the angled lines in the red and yellow regions
    arcade.draw_line(120, 175+(50*i), 250, 100+(50*i), arcade.color.BLACK, 5)
    arcade.draw_line(250, 100+(50*i), 380, 175+(50*i), arcade.color.BLACK, 5)

for i in range(7):  # #Draws all of the vertical lines
    if i <= 3:
        arcade.draw_line(120+(43.3*i), 325-(25*i), 120+(43.3*i), 175-(25*i), arcade.color.BLACK, 5)
    elif i >= 4:    # # IF/ELSE allows the program to adjust the vertical positioning of the vertical lines
        arcade.draw_line(120+(43.3*i), 325-150+(25*i), 120+(43.3*i), 175-150+(25*i), arcade.color.BLACK, 5)

arcade.finish_render()
arcade.run()