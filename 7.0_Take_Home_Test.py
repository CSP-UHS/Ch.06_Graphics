'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________

Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade
arcade.open_window(500,400,"Take Home Test")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
for x_offset in range(0,501,20):
    arcade.draw_line(x_offset,0,x_offset,400,arcade.color.BLACK)
for y_offset in range(0,401,20):
    arcade.draw_line(0,y_offset,500,y_offset,arcade.color.BLACK)
arcade.draw_rectangle_filled(50,370,60,20,arcade.color.PHLOX)
arcade.draw_rectangle_filled(200,260,40,20,arcade.color.BLUSH,45)
arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA)
arcade.draw_ellipse_filled(100,100,60,20,arcade.color.AMBER)
arcade.draw_line(80,20,120,60,arcade.color.BLUE,1)
arcade.draw_text("I love you. I know.",20,160,arcade.color.BRICK_RED,20)
arcade.draw_arc_filled()
arcade.finish_render()
arcade.run()

