#Sign your name:____Emma Moritz_____

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500, 400, "Star Wars Art")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

for x_offset in range(0,500,21):
    arcade.draw_line(0+x_offset,0,0+x_offset,500,arcade.color.BLACK,1)
for y_offset in range(0,500,21):
    arcade.draw_line(0,0+y_offset,500,0+y_offset,arcade.color.BLACK,1)
arcade.draw_rectangle_filled(52,367,64,20,arcade.color.PHLOX)
arcade.draw_rectangle_filled(210,273,41,21,arcade.color.BLUSH,45)
arcade.draw_circle_filled(260,210,42,arcade.color.WISTERIA)
arcade.draw_arc_filled(400, 315, 64, 64, arcade.color.YELLOW,30,330)
arcade.draw_text("I love you. I know.",22,164,)#finnish

arcade.finish_render()
arcade.run()
#amber=oval yellow=packman Brickred=words and angled rec  wishteria=circle  blue=;line