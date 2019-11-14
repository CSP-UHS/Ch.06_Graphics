#Sign your name: Tristan

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500,400,"Star Wars Art")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
x=0
y=0
for i in range(25):
    arcade.draw_line(0, y, 500, y, arcade.color.BLACK)
    y+=20
for i in range(25):
    arcade.draw_line(x, 0, x, 400, arcade.color.BLACK)
    x+=20
arcade.draw_line(80,20,120,60,arcade.color.BLUE)
arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)
arcade.draw_rectangle_filled(50, 370, 60, 20, arcade.color.PHLOX)
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, 45)
arcade.draw_text("I love you. I know.",20, 160, arcade.color.BRICK_RED,20)
arcade.draw_ellipse_filled(100,100,60,20,arcade.color.AMBER)
arcade.draw_arc_filled(400,320,60,60,arcade.color.YELLOW,30,330,0)
arcade.draw_rectangle_filled(460,10,5,5,arcade.color.RED)
arcade.finish_render()
arcade.run()
