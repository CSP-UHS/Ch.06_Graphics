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
import arcade;arcade.open_window(500,500,"Dylan Smith");i=0;offset=25;T=0
arcade.set_background_color(arcade.color.BLACK);arcade.start_render()
#Shoulders
arcade.draw_arc_filled(250,0,250,175,(0,128,255),0,180)
arcade.draw_line(75,60,75,0,arcade.color.BLACK);arcade.draw_line(425,60,425,0,arcade.color.BLACK)
#Skull Base
arcade.draw_circle_filled(250,320,130,arcade.color.WHITE);arcade.draw_circle_filled(250,245,125,arcade.color.WHITE)
#Eyeholes
for x_offset in range(100,350,140):
    arcade.draw_ellipse_filled(80+x_offset,320,40,30,arcade.color.BLACK)
#Iris'
arcade.draw_circle_filled(180,320,20,arcade.color.WHITE);arcade.draw_circle_filled(320,320,20,(102,255,255))
#Pupil's
for x_offset in range(100,350,140):
    arcade.draw_circle_filled(80+x_offset,320,8,arcade.color.BLACK)
#Eye detail
arcade.draw_text("*",325,300,arcade.color.WHITE,40)
#Nose
arcade.draw_triangle_filled(230,255,270,255,250,285,arcade.color.BLACK)
#Main Mouth Outside
arcade.draw_arc_outline(250,230,70,60,arcade.color.BLACK,180,360,8);arcade.draw_line(170,225,330,225,arcade.color.BLACK,8)
#Cheek Bones
arcade.draw_arc_filled(170,235,20,20,arcade.color.WHITE,270,360);arcade.draw_arc_filled(330,235,20,20,arcade.color.WHITE,180,270)
#Teeth
for x_offset in range(170,300,20):
    if T >-1 and T<3:
        arcade.draw_line(20+x_offset,222,20+x_offset,200-i,arcade.color.BLACK)
        i+=15
        T+=1
    elif T >=3:
        arcade.draw_line(20 + x_offset, 222, 20 + x_offset, 215-i, arcade.color.BLACK)
        i-=7.5
        T+=1




arcade.finish_render();arcade.run()