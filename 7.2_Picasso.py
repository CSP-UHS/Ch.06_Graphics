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
arcade.open_window(500, 400, "Lily Burkhead")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
x_offset=0
for i in range(25):
    arcade.draw_line(x_offset,0,x_offset,400,arcade.color.WHITE)
    x_offset+=20
y_offset=0
for i in range(20):
    arcade.draw_line(0,y_offset,500,y_offset,arcade.color.WHITE)
    y_offset+=20
arcade.draw_circle_filled(250,250,80,arcade.color.ASH_GREY)
arcade.draw_rectangle_filled(250,160,160,195,arcade.color.WHITE)
arcade.draw_rectangle_filled(190,53,40,23,arcade.color.WHITE)
arcade.draw_rectangle_filled(310,53,40,23,arcade.color.WHITE)
arcade.draw_rectangle_filled(250,310,20,40,arcade.color.DARK_BLUE)
arcade.draw_circle_filled(250,310,10,arcade.color.CHARTREUSE)
arcade.draw_rectangle_filled(195,280,20,30,arcade.color.DARK_BLUE)
arcade.draw_ellipse_filled(230,280,10,15,arcade.color.DARK_BLUE)
arcade.draw_ellipse_filled(270,275,20,15,arcade.color.DARK_BLUE)
arcade.draw_circle_filled(270,275,10,arcade.color.RED)
arcade.draw_rectangle_filled(250,260,160,10,arcade.color.DARK_BLUE)
arcade.draw_rectangle_filled(305,280,20,30,arcade.color.DARK_BLUE)
arcade.draw_rectangle_filled(250,65,160,15,arcade.color.DARK_BLUE)
y_offset=245
for i in range (3):
    arcade.draw_rectangle_filled(250,y_offset,80,10,arcade.color.DARK_BLUE)
    y_offset-=20
x_offset=210
for i in range (3):
    arcade.draw_ellipse_filled(x_offset,150,10,40,arcade.color.DARK_BLUE)
    x_offset+=40
arcade.draw_ellipse_outline(180,180,10,60,arcade.color.BLACK,2)
arcade.draw_ellipse_outline(320,180,10,60,arcade.color.BLACK,2)
arcade.draw_circle_filled(250,90,10,arcade.color.DARK_BLUE)
arcade.draw_text("R2D2 Drawing",20,380,arcade.color.WHITE,10)
arcade.draw_ellipse_outline(210,90,15,10,arcade.color.BLACK,2)
x_offset=185
for i in range(8):
    arcade.draw_line(x_offset,57,x_offset,75,arcade.color.WHITE,2)
    x_offset+=20
arcade.draw_rectangle_filled(180,100,15,25,arcade.color.DARK_BLUE)
arcade.draw_ellipse_filled(290,90,15,10,arcade.color.DARK_BLUE)
arcade.draw_circle_outline(320,90,10,arcade.color.BLACK,2)
arcade.finish_render()
arcade.run()
