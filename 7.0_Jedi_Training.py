#Sign your name:Ian Neyens

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade
arcade.open_window(500, 400, "Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

for vert_line in range(20, 500, 20):
    arcade.draw_line(vert_line, 0, vert_line, 500, arcade.color.BLACK)
for horiz_line in range(20, 500, 20):
    arcade.draw_line(0, horiz_line, 500, horiz_line, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(20, 80, 380, 360, arcade.color.PHLOX)
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER)
arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)
arcade.draw_rectangle_filled(200, 260, 20, 40, arcade.color.BLUSH, 45)
arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 30, 330, 0)
arcade.draw_rectangle_filled(460, 10, 5, 5, arcade.color.RED)
arcade.draw_text("I love you. I know.", 20, 155, arcade.color.BRICK_RED, 21)

arcade.finish_render()
arcade.run()
