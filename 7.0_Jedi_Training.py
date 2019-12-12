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

arcade.draw_rectangle_filled(70,450,80,25, arcade.color.PHLOX)
arcade.draw_line(100,40,120,60, arcade.color.BLACK)
arcade.draw_text("I love you. I know",40,230, arcade.color.BRICK_RED,20)
arcade.draw_ellipse_filled(100,100,80,20, arcade.color.AMBER)
arcade.draw_circle_filled(280,270,45,arcade.color.WISTERIA)
arcade.draw_arc_filled(400,320,60,60,arcade.color.YELLOW,30,330)
arcade.draw_rectangle_filled(200,320,40,20,arcade.color.BLUSH,45)
arcade.finish_render()

arcade.run()
