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
import random
t=185
x=50
y=600
r=5
z=random.randrange(1,6)
arcade.open_window(700, 700, "Tristan Holman", True)
arcade.set_background_color(arcade.color.SKY_BLUE)
arcade.start_render()
#Background
arcade.draw_lrtb_rectangle_filled(0,700,280,0,(112,176,0))
for i in range(z):
    for i in range (2):
        for i in range(r):
            arcade.draw_circle_filled(x,y,25,arcade.color.WHITE_SMOKE)
            x+=20
        y+=20
        x-=90
        r=4
    r=5
    x=random.randrange(0,701)
    y=random.randrange(500,670)
#Shadow
arcade.draw_ellipse_filled(350,200,240,30,arcade.color.BLACK)
arcade.draw_ellipse_outline(350,200,240,30,arcade.color.BLACK,15)
#Base
arcade.draw_circle_filled(350,385,200,arcade.color.RED)
arcade.draw_arc_filled(350,385,200,200,arcade.color.WHITE,0,180,180)
#Tint
arcade.draw_circle_filled(350,460,100,(235,0,0))
arcade.draw_circle_filled(375,500,20,(225,220,220))
arcade.draw_circle_outline(375,500,20,(225,220,220))
for i in range(3):
    arcade.draw_arc_outline(350,390,200,t,(205,205,205),0,180,1000,180)
    t+=5
#Middle
arcade.draw_rectangle_filled(350,385,400,30,arcade.color.BLACK)
arcade.draw_circle_filled(350,385,60,arcade.color.BLACK)
arcade.draw_circle_outline(350,385,60,arcade.color.BLACK)
arcade.draw_circle_filled(350,385,40,arcade.color.WHITE)
arcade.draw_circle_outline(350,385,40,arcade.color.WHITE)
arcade.draw_circle_outline(350,385,25,arcade.color.BLACK, 5)
#Finish Outline
arcade.draw_circle_outline(350,385,200,arcade.color.BLACK,10)
#Grid
"""
x=0
y=0
for i in range(35):
    arcade.draw_line(0, y, 700, y, arcade.color.BLACK)
    y+=20
for i in range(35):
    arcade.draw_line(x, 0, x, 700, arcade.color.BLACK)
    x+=20
"""
arcade.finish_render()
arcade.run()
