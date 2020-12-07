#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500,400,"Drawling")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()


arcade.draw_rectangle_filled(50,370,60,20,arcade.color.PHLOX)

arcade.draw_line(80,20,120,60,arcade.color.BLUE)
arcade.draw_text("I love you. I know",20,160,arcade.color.BLUSH,12)


arcade.finish_render()
arcade.run()