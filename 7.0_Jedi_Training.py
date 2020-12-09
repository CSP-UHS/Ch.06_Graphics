# #Sign your name: Ryan Muetzel

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade

arcade.open_window(500, 400, "Jedi Training")
arcade.set_background_color((239, 222, 204))

arcade.start_render()

for i in range (25):
    arcade.draw_line(0, i*20, 750, i*20, arcade.color.BLACK, 1.2)
    arcade.draw_line(i*20, 0, i*20, 600, arcade.color.BLACK, 1.2)

arcade.draw_lrtb_rectangle_filled(20, 80, 380, 360, arcade.color.MAGENTA)
arcade.draw_ellipse_filled(100, 100, 120, 40, (255, 192, 0))
#arcade.draw_circle_filled(460, 10, 5, arcade.color.ALIZARIN_CRIMSON)
arcade.draw_rectangle_filled(460, 10, 6, 6, arcade.color.ALIZARIN_CRIMSON)
arcade.draw_circle_filled(250, 200, 40, (202, 158, 222))
arcade.draw_rectangle_filled(200, 260, 20, 40, (224, 91, 130), 45)
arcade.draw_line(80, 20, 120, 60, (85, 74, 238), 1)
arcade.draw_arc_filled(400, 320, 120, 120, (255, 255, 0), 30, 330, 0)
arcade.draw_text('I love you. I know.', 20, 155, (207, 74, 90), 20)

arcade.finish_render()

arcade.run()
