#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500, 400, "Drawing")
arcade.set_background_color((239, 222, 204))
arcade.start_render()
#Drawing commands
for loo in range(0, 400, 20):
    arcade.draw_line(0, 20+loo, 500, 20+loo, (0, 0, 0), 1)
for loo in range(0, 500, 20):
    arcade.draw_line(20+loo, 0, 20+loo, 500, (0, 0, 0), 1)
arcade.draw_line(80, 20, 120, 60, (108, 95, 231))
arcade.draw_rectangle_filled(460, 10, 4, 4, (237, 56, 51), 0)
arcade.draw_rectangle_filled(50, 370, 60, 20, (229, 87, 249), 0)
arcade.draw_rectangle_filled(200, 260, 40, 20, (225, 91, 131), 140)
arcade.draw_circle_filled(250, 200, 40, (202, 158, 221), 1)
arcade.draw_text("I love you. I know.", 20, 154, (240, 75, 62), 21)
arcade.draw_ellipse_filled(100, 100, 120, 40, (248, 193, 69), 1)
arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 30, 330)

arcade.finish_render()
arcade.run()

