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
arcade.open_window(625, 625, "The USS Enterprise")
arcade.set_background_color(arcade.color.BLACK)
x=30
y=30
circle=13
radius=110
angle=0
arcade.start_render()

arcade.draw_rectangle_filled(240,360, 25,100,arcade.color.GRAY,30)
arcade.draw_rectangle_filled(240, 240, 25, 100, arcade.color.GRAY, -30)
arcade.draw_rectangle_filled(340,300,80,60,arcade.color.GRAY)
arcade.draw_rectangle_filled(255,300,100,30,arcade.color.GRAY)
arcade.draw_rectangle_filled(240, 240, 100, 6, arcade.color.AERO_BLUE, 60)
arcade.draw_rectangle_filled(240,360,100,6,arcade.color.AERO_BLUE,-60)
arcade.draw_rectangle_filled(255,315,100,20,arcade.color.GRAY,7)
arcade.draw_rectangle_filled(255, 285, 100, 20, arcade.color.GRAY, -7)
arcade.draw_circle_filled(205,300,19,arcade.color.GRAY)
arcade.draw_rectangle_filled(340,300,60,50,arcade.color.LIGHT_GRAY)
arcade.draw_rectangle_filled(260,310,105,20,arcade.color.LIGHT_GRAY,7)
arcade.draw_rectangle_filled(260, 290, 105, 20, arcade.color.LIGHT_GRAY, -7)
arcade.draw_circle_filled(210,300,15,arcade.color.LIGHT_GRAY)
arcade.draw_lrtb_rectangle_filled(310,400,305,295,arcade.color.GRAY)




arcade.draw_circle_filled(480,300,120,arcade.color.LIGHT_GRAY)
arcade.draw_circle_outline(480,300,120,arcade.color.GRAY)
for i in range(7):
    arcade.draw_circle_outline(480,300,radius, arcade.color.GRAY)
    radius -= circle


for i in range(16):
    arcade.draw_line(480,332,480,420,arcade.color.GRAY,.5)
    arcade.draw_line(505,322,565,385,arcade.color.GRAY,.5)
    arcade.draw_line(512,300,600,300,arcade.color.GRAY,.5)
    arcade.draw_line(505,278,565,215,arcade.color.GRAY,.5)
    arcade.draw_line(480,268,480,180,arcade.color.GRAY,.5)
    arcade.draw_line(457,278,394,215,arcade.color.GRAY,.5)
    arcade.draw_line(457, 322, 394, 385, arcade.color.GRAY, .5)
    arcade.draw_line(450, 300, 420,300,arcade.color.GRAY,.5)
    arcade.draw_circle_filled(420,300,5,arcade.color.GRAY)
    arcade.draw_rectangle_filled(412,300,15,8,arcade.color.GRAY)
    arcade.draw_circle_filled(390,300,15,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(370,300,40,30,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(370,300,38,28,arcade.color.GRAY)
    arcade.draw_circle_filled(390, 300, 14, arcade.color.GRAY)
    arcade.draw_circle_filled(490,300,15,arcade.color.GRAY)
    arcade.draw_circle_filled(470,300,10,arcade.color.GRAY)
    arcade.draw_rectangle_filled(480,310,18,7,arcade.color.GRAY,15)
    arcade.draw_rectangle_filled(480,290,18,7,arcade.color.GRAY,-15)
    arcade.draw_circle_filled(490,300,10,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(200,195,20,300,arcade.color.LIGHT_GRAY,90)
    arcade.draw_rectangle_filled(200,405,20,300,arcade.color.LIGHT_GRAY,90)
    arcade.draw_triangle_filled(15, 405, 50, 395, 50, 415, arcade.color.LIGHT_GRAY)
    arcade.draw_triangle_filled(15, 195, 50, 185, 50, 205, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(350, 195, 10, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(350, 405, 10, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(390,300,8,arcade.color.CAPRI)
    arcade.draw_rectangle_filled(200,195, 16, 290, arcade.color.GRAY,90)
    arcade.draw_rectangle_filled(200,405,16,290,arcade.color.GRAY,90)
    arcade.draw_circle_filled(348,195,8,arcade.color.GRAY)
    arcade.draw_circle_filled(348,405,8,arcade.color.GRAY)
    arcade.draw_triangle_filled(25,405,55,397,55, 413,arcade.color.GRAY)
    arcade.draw_triangle_filled(25,195,55,187,55,203,arcade.color.GRAY)
    arcade.draw_circle_filled(310,195,3,arcade.color.CAPRI)
    arcade.draw_circle_filled(310, 405, 3, arcade.color.CAPRI)
arcade.finish_render()
arcade.run()

