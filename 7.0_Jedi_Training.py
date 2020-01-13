#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade

arcade.open_window(500,500, "jedi training")
arcade.set_background_color(arcade.color.ALMOND)

arcade.start_render()
# variable
x1 = 0
y1 = 500
x2 = 500
y2 = 500
for i in range (25):
    arcade.draw_line(x1,y1,x2,y2, arcade.color.BLACK,1)
    y2-=20
    y1-=20
#variabless 2
a1=0
b1=500
a2=0
b2=0
for i in range (25):
    arcade.draw_line(a1,b1,a2,b2,arcade.color.BLACK,1)
    a1+=20
    a2+=20


arcade.draw_rectangle_filled(70,450,80,20, arcade.color.PHLOX)
arcade.draw_line(100,40,140,60, arcade.color.BLACK)
arcade.draw_text("I love you. I know",20,230, arcade.color.BRICK_RED,20)
arcade.draw_ellipse_filled(100,100,60,20, arcade.color.AMBER)
arcade.draw_circle_filled(260,270,45,arcade.color.WISTERIA)
arcade.draw_arc_filled(400,420,60,60,arcade.color.YELLOW,30,330)
arcade.draw_rectangle_filled(200,320,40,20,arcade.color.BLUSH,45)

arcade.finish_render()

arcade.run()
