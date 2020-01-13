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
import random


random.randint(420,480)

arcade.open_window(500,500,"Zach Cobb")
arcade.set_background_color(arcade.color.STAR_COMMAND_BLUE)
arcade.start_render()
#alien

arcade.draw_ellipse_filled(250,250,150,220, arcade.color.GREEN)
arcade.draw_ellipse_filled(320,320,40,60, arcade.color.BLACK,-35)
arcade.draw_ellipse_filled(180,320,40,60,arcade.color.BLACK,35)
arcade.draw_parabola_outline(200,50,300,50, arcade.color.BLACK,2)
#nose
arcade.draw_ellipse_filled(270,240,5,10, arcade.color.BLACK,-25)
arcade.draw_ellipse_filled(230,240,5,10,arcade.color.BLACK,25)

#antennas
arcade.draw_rectangle_filled(180,460,15,45,arcade.color.GREEN,25)
arcade.draw_rectangle_filled(320,460,15,45,arcade.color.GREEN,-25)
arcade.draw_circle_filled(170,480,10,arcade.color.RED)
arcade.draw_circle_filled(330,480,10,arcade.color.RED)
# stars
n=0
for i in range(5):
    arcade.draw_circle_filled(random.randint(20,60),random.randint(20,480),random.randint(2,10),arcade.color.WHITE)
    arcade.draw_circle_filled(random.randint(420,480),random.randint(20,480),random.randint(2,10),arcade.color.WHITE)





# variable
x1 = 0
y1 = 500
x2 = 500
y2 = 500
for i in range (25):
    arcade.draw_line(x1,y1,x2,y2, arcade.color.BLACK,1)
    y2-=20
    y1-=20

#variables 2
a1=0
b1=500
a2=0
b2=0
for i in range (25):
    arcade.draw_line(a1,b1,a2,b2,arcade.color.BLACK,1)
    a1+=20
    a2+=20






arcade.finish_render()
arcade.run()


