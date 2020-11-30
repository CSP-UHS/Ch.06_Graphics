#Sign your name:Alex Mears

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade

hor_line_count = 0
vert_line_count = 0
x = 0
y = 0
arcade.open_window(1000, 800, "Test image")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
while hor_line_count <= 20:
    arcade.draw_line(0, y, 1000, y, arcade.color.BLACK, 1)
    y += 40
    hor_line_count += 1
while vert_line_count <= 25:
    arcade.draw_line(x, 0, x, 800, arcade.color.BLACK, 1)
    x += 40
    vert_line_count += 1
arcade.draw_rectangle_filled(100, 740, 120, 40, arcade.color.PHLOX, 0)
arcade.draw_ellipse_filled(200, 200, 240, 80, arcade.color.AMBER, 0, 0)
arcade.draw_circle_filled(500, 400, 80, arcade.color.WISTERIA, 0)
arcade.draw_rectangle_filled(400, 520, 80, 40, arcade.color.BLUSH, -45)
arcade.draw_rectangle_filled(920, 20, 10, 10, arcade.color.BRICK_RED, 0)
arcade.draw_arc_filled(800, 640, 240, 240, arcade.color.YELLOW, 30, 330, 0, 128)
arcade.draw_text("I love you. I know.", 40, 307, arcade.color.BRICK_RED, 45, 420, "left",)
arcade.finish_render()
arcade.run()