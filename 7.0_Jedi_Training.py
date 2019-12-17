#Sign your name: Caleb Hews

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade
arcade.open_window(500,400,"Ch. 7 Jedi training")
arcade.set_background_color(arcade.color.ALMOND)
x=20
y=20
arcade.start_render()

for x in range(0,600,20):
    arcade.draw_line(20+x, 400, 20+x, 0, arcade.color.BLACK, 1)
for y in range(0,600,20):
    arcade.draw_line(0,20+y, 500, 20+y, arcade.color.BLACK, 1)
arcade.draw_lrtb_rectangle_filled(20, 80, 380, 360,arcade.color.PHLOX)
arcade.draw_rectangle_filled(200, 260,40,20, arcade.color.BLUSH, 45)
arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)
arcade.draw_ellipse_filled(100,100,60, 20, arcade.color.AMBER)
arcade.draw_arc_filled(400, 320, 60, 60, arcade.color.YELLOW,30,330)
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE, 1)
arcade.draw_text("I love you. I know.",20,160,arcade.color.BRICK_RED, 20)
arcade.draw_rectangle_filled(460,10,5,5,arcade.color.RED)
arcade.finish_render()
arcade.run()