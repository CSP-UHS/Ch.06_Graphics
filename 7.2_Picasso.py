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

arcade.open_window(600,600,"Malsawmthara Hmar")
arcade.set_background_color(arcade.color.WHITE_SMOKE)
arcade.start_render()

x_offset=0
y_offset=0
for i in range(30):
    x_offset+=20
    arcade.draw_line(x_offset,0,x_offset,600,arcade.color.BLACK)  #draw the vertical lines
for i in range(30):
    y_offset+=20
    arcade.draw_line(0,y_offset,600,y_offset,arcade.color.BLACK)  #draw the horizontal lines
arcade.draw_rectangle_outline(300,10,110,20,arcade.color.BLACK,5) #midle bottom block
arcade.draw_rectangle_outline(318,10,10,20,arcade.color.BLACK,5)  #little block on the right
arcade.draw_rectangle_outline(282,10,10,20,arcade.color.BLACK,5)    #little block on the left
arcade.draw_rectangle_outline(300,125,44,210,arcade.color.BLACK,5)  #biggest block behind
arcade.draw_rectangle_filled(300,45,90,50,arcade.color.WHITE)
arcade.draw_rectangle_outline(300,45,90,50,arcade.color.BLACK,5)    #big middle block
arcade.draw_rectangle_filled(280,100,30,160,arcade.color.WHITE)
arcade.draw_rectangle_outline(280,100,30,160,arcade.color.BLACK,5)   #left block at front
arcade.draw_rectangle_filled(320,100,30,160,arcade.color.WHITE)
arcade.draw_rectangle_outline(320,100,30,160,arcade.color.BLACK,5)   #right block at front
arcade.draw_rectangle_filled(281,200,20,40,arcade.color.WHITE)
arcade.draw_rectangle_outline(281,200,20,40,arcade.color.BLACK,5)   #left block at front
arcade.draw_rectangle_filled(319,200,20,40,arcade.color.WHITE)
arcade.draw_rectangle_outline(319,200,20,40,arcade.color.BLACK,5)    #Right block at front
arcade.draw_rectangle_filled(300,235,28,10,arcade.color.WHITE)
arcade.draw_rectangle_outline(300,235,28,10,arcade.color.BLACK,5)   #Top block
arcade.draw_line(300,240,300,280,arcade.color.BLACK,5)  #top line



arcade.finish_render()
arcade.run()


