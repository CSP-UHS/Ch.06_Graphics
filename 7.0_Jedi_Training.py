# Sign your name: Gerardo Lopez

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade

arcade.open_window(500, 400, "The Stars and Stripes")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
for x_offset in range(20, 500, 20):
    arcade.draw_rectangle_filled(0 + x_offset, 0, 2, 800, arcade.color.BLACK)
    arcade.draw_rectangle_filled(0, 0 + x_offset, 1000, 2, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(20, 80, 380, 360, arcade.color.PHLOX)
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, 315)
arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA)
arcade.draw_arc_filled(400, 320, 120, 120,arcade.color.YELLOW, 30, 325)
arcade.draw_text("I love you. I know.", 20, 154, arcade.color.BRICK_RED, 20, 220)
arcade.draw_arc_filled(100, 100, 120, 40, arcade.color.AMBER, 0, 360)
arcade.draw_line(120, 60, 80, 20, arcade.color.BLUE)
arcade.draw_point(460, 10, arcade.color.RED, 10)
arcade.finish_render()
arcade.run()
