#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.\
'''
import arcade

arcade.open_window(500,400,"Jedi Training")
arcade.set_background_color((239, 222, 205))

arcade.start_render()
for x_off in range(0,500,20):
    arcade.draw_line((x_off), 0, (x_off), 400, arcade.color.BLACK, 2)

for y_off in range(0,400,20):
    arcade.draw_line(0, (y_off), 500, (y_off), arcade.color.BLACK, 2)

arcade.draw_lrtb_rectangle_filled(20, 80, 380, 360, (223, 0, 255))

arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE, 1)

arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)

arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER)

arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, 135)

arcade.draw_text("I love you. I know.", 45, 155, arcade.color.BRICK_RED, 20)

arcade.draw_arc_filled(320, 320, 120, 120, arcade.color.YELLOW, 340, 20, 0, 128)

arcade.finish_render()

arcade.run()